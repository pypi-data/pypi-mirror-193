"""AWS lambda utilities."""
from __future__ import annotations
from asyncio import sleep, wait_for
from base64 import b64encode as _b64encode
from copy import deepcopy
from datetime import datetime, timezone
from os import urandom
from typing import Any, Literal, Dict
from botocore.config import Config
from botocore.exceptions import ClientError
from jhalog import LogEvent, LogEventNotFoundException
from starlette.exceptions import HTTPException
from starlette.responses import Response
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE, HTTP_429_TOO_MANY_REQUESTS
from starlette_aws_lambda_api_client._session import Session


HttpMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]

_DEFAULT_REQUEST_PAYLOAD: Dict[str, Any] = dict(
    version="2.0",
    routeKey="$default",
    rawQueryString="",
    isBase64Encoded=False,
    headers={
        "content-type": "application/json; charset=utf-8",
    },
    requestContext=dict(
        http=dict(protocol="HTTP/1.1"),
        routeKey="$default",
        stage="$default",
    ),
)
_RETRY_DELAY_SECONDS = 0.25
_RETRY_COUNT = 5
_RETRYABLE_ERRORS = {
    "CodeArtifactUserPendingException",
    "ResourceNotReadyException",
    "ServiceException",
    "EC2ThrottledException",
    "SubnetIPAddressLimitReachedException",
    "ENILimitReachedException",
}


class InvokedLambdaFunctionError(Exception):
    """Error from an invoked lambda function."""


class LambdaApiClient:
    """Lambda API client."""

    #: Global default timeout
    DEFAULT_TIMEOUT = 900

    __slots__ = (
        "_session",
        "_duration",
        "_config",
        "_role_arn",
        "_region_name",
        "_timeout",
        "_function_name",
        "_queue_url",
        "_payload",
        "_json_loads",
        "_json_dumps",
    )

    def __init__(
        self,
        session: Session,
        function_name: str,
        queue_url: str | None = None,
        region_name: str | None = "",
        role_arn: str | None = "",
        duration: int = 3600,
        config: Config | None = None,
        timeout: int | None = None,
        user_agent: str | None = None,
    ) -> None:
        """Lambda client initialization.

        Args:
            session: Session.
            function_name: Lambda function name.
            queue_url: If the function can be invoked through a SQS queue,
                the URL of this queue.
            role_arn: Role to assume. If not specified, does not assume role.
                Explicitly pass None to enforce not using the default role.
            region_name: Region name to use. If not specified use default region.
                Explicitly pass None to enforce not using the default region.
            duration: Expiration in seconds for assumed roles.
            config: Clients config to use. If not specified, use the default config.
            timeout: Default function invocation timeout.
            user_agent: If specified, the user agent
        """
        self._function_name = function_name
        self._session = session
        self._config = config
        self._region_name = region_name
        self._role_arn = role_arn
        self._duration = duration
        self._timeout = timeout or self.DEFAULT_TIMEOUT
        self._queue_url = queue_url
        self._payload = deepcopy(_DEFAULT_REQUEST_PAYLOAD)
        if user_agent:
            self._payload["requestContext"]["http"]["userAgent"] = user_agent
            self._payload["headers"]["user-agent"] = user_agent
        self._json_loads = self._session._json_loads
        self._json_dumps = self._session._json_dumps

    async def _client(self) -> Any:
        """AioBoto3 lambda client.

        Returns:
            Client.
        """
        return await self._session.client(
            "lambda",
            region_name=self._region_name,
            role_arn=self._role_arn,
            config=self._config,
            duration=self._duration,
        )

    async def _invoke(self, payload: str, timeout: int | None = None) -> Any:
        """Invoke the lambda function.

        Args:
            payload: Function payload.
            timeout: Function timeout. If not specified, used default timeout.

        Returns:
            Response.
        """
        client = await self._client()
        timeout = timeout or self._timeout
        retries = 0
        while True:
            try:
                return await wait_for(
                    client.invoke(FunctionName=self._function_name, Payload=payload),
                    timeout,
                )
            except ClientError as exception:  # pragma: no cover
                code = exception.response["Error"]["Code"]
                if code in _RETRYABLE_ERRORS:
                    if retries > _RETRY_COUNT:
                        self._log_exception(exception)
                        raise HTTPException(status_code=HTTP_503_SERVICE_UNAVAILABLE)
                    retries += 1
                    await sleep(_RETRY_DELAY_SECONDS * retries**2)
                    continue
                elif code == "TooManyRequestsException":
                    self._log_exception(exception)
                    raise HTTPException(status_code=HTTP_429_TOO_MANY_REQUESTS)
                raise

    async def request(
        self,
        path: str,
        body: Any | None = None,
        *,
        headers: dict[str, str] | None = None,
        method: HttpMethod = "GET",  # noqa
        params: dict[str, str] | None = None,
        timeout: int | None = None,
    ) -> Response:
        """Invoke lambda function using AWS API Gateway v2 payload format.

        Args:
            path: API path. If not specified, use body as payload directly instead of
                using API Gateway format.
            body: Body. Must be JSON serializable.
            headers: Request HTTP headers.
            method: HTTP method.
            params: Query parameters.
            timeout: Function timeout. If not specified, used default timeout.

        Returns:
            Response.
        """
        body = self._prepare_request(
            path=path, method=method, body=body, headers=headers, params=params
        )
        resp_payload = self._json_loads(
            (
                await (
                    await self._invoke(payload=self._json_dumps(body), timeout=timeout)
                )["Payload"].read()
            ).decode(errors="ignore")
        )

        self._handle_lambda_error(resp_payload)

        status_code = int(resp_payload["statusCode"])
        resp_body = resp_payload["body"]
        resp_body = resp_body if resp_body != "null" else None
        if status_code >= 400:
            detail = self._json_loads(resp_body)
            if isinstance(detail, dict) and "detail" in detail:
                detail = detail["detail"]
            raise HTTPException(status_code=status_code, detail=detail)
        return Response(status_code=status_code, content=resp_body)

    async def send_to_queue(
        self,
        path: str,
        body: Any | None = None,
        *,
        headers: dict[str, str] | None = None,
        method: HttpMethod = "GET",  # noqa
        params: dict[str, str] | None = None,
    ) -> None:
        """Invoke lambda function via SQS queue using AWS API Gateway v2 payload format.

        Args:
            path: API path. If not specified, use body as payload directly instead of
                using API Gateway format.
            body: Body. Must be JSON serializable.
            headers: Request HTTP headers.
            method: HTTP method.
            params: Query parameters.
        """
        if not self._queue_url:
            raise RuntimeError('No "queue_url" specified on class instantiation.')
        client = await self._session.client(
            "sqs",
            region_name=self._region_name,
            role_arn=self._role_arn,
            config=self._config,
            duration=self._duration,
        )
        await client.send_message(
            QueueUrl=self._queue_url,
            MessageBody=self._json_dumps(
                self._prepare_request(
                    path=path, method=method, body=body, headers=headers, params=params
                )
            ),
        )

    def _prepare_request(
        self,
        path: str,
        body: Any | None,
        headers: dict[str, str] | None,
        method: HttpMethod,  # noqa
        params: dict[str, str] | None,
    ) -> dict[str, Any]:
        """Prepare a request in API Gateway v2 payload format.

        Args:
            path: API path.
            body: Body. Must be JSON serializable.
            headers: Request HTTP headers.
            method: HTTP method.
            params: Query parameters.

        Returns:
            Request payload.
        """
        req_payload: dict[str, Any] = deepcopy(self._payload)
        req_context: dict[str, Any] = req_payload["requestContext"]
        req_headers = req_payload["headers"]
        req_http: dict[str, str] = req_context["http"]

        req_payload["body"] = self._json_dumps(body)
        req_headers["content-length"] = str(len(req_payload["body"]))

        req_payload["rawPath"] = req_http["path"] = path
        req_http["method"] = method

        if params:
            req_payload["queryStringParameters"] = params
            req_payload["rawQueryString"] = "&".join(
                f"{key}={value}" for key, value in params.items()
            )

        if headers:
            for key, value in headers.items():
                req_headers[key.lower()] = value

        req_context["requestId"] = (
            self._get_request_id() or _b64encode(urandom(12)).decode()
        )
        now = datetime.now(timezone.utc)
        req_context["time"] = now.isoformat()
        req_context["timeEpoch"] = now.timestamp()
        return req_payload

    @staticmethod
    def _handle_lambda_error(resp_payload: Dict[str, Any]) -> None:
        """Handle AWS lambda errors if any.

        Args:
            resp_payload: Lambda response payload.
        """
        if "errorMessage" in resp_payload:  # pragma: no cover
            try:
                raise InvokedLambdaFunctionError(
                    "\n".join(
                        (
                            "An exception occurred in the invoked lambda function:",
                            "\nTraceback (most recent call last):",
                            "".join(resp_payload["stackTrace"]).rstrip(),
                            (
                                f"{resp_payload['errorType']}:"
                                f" {resp_payload['errorMessage']}"
                            ),
                        )
                    )
                )
            except KeyError:
                raise InvokedLambdaFunctionError(
                    "\n".join(
                        (
                            "An error occurred when invoking the lambda function:",
                            resp_payload["errorMessage"],
                        )
                    )
                )

    @staticmethod
    def _log_exception(exception: Exception) -> None:
        """Add "error_detail" field to current context log event.

        Args:
            exception: Exception.
        """
        try:
            LogEvent.from_context().error_detail_from_exception(exception)
        except LogEventNotFoundException:
            return

    @staticmethod
    def _get_request_id() -> str | None:
        """Get request ID from current context log event.

        Returns:
            Request ID
        """
        return LogEvent.get_from_context("request_id")  # type: ignore
