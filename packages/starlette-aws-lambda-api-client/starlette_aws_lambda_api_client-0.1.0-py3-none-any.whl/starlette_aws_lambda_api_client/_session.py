"""AWS common utilities."""
from asyncio import gather
from datetime import datetime, timezone, timedelta
from typing import Any, Optional, TYPE_CHECKING, Callable
from socket import gethostname
from botocore.client import Config
from aioboto3 import Session as AioBoto3Session
from starlette_aws_lambda_api_client._json import loads, dumps, JSONDecodeError


if TYPE_CHECKING:
    from mypy_boto3_sts.literals import ServiceName


class Session:
    """AWS Session.

    Features clients caching, easy assume role, automatic STS session renew.
    """

    __slots__ = (
        "_session",
        "_clients",
        "_config",
        "_role_arn",
        "_region_name",
        "_json_loads",
        "_json_dumps",
    )

    #: Default clients config
    DEFAULT_CONFIG = Config(
        parameter_validation=False,
        retries=dict(mode="standard"),
    )

    def __init__(
        self,
        session: Optional[AioBoto3Session] = None,
        config: Optional[Config] = None,
        region_name: Optional[str] = None,
        role_arn: Optional[str] = None,
        json_loads: Callable[..., Any] = loads,
        json_dumps: Callable[..., str] = dumps,
        speedup: bool = True,
    ) -> None:
        """Initialize session.

        Args:
            session: AioBoto3 session. If not specified, create a new session.
            config: Clients default config to use. Merged with "Session.DEFAULT_CONFIG".
            region_name: Clients default region to use.
            role_arn: Clients default role ARN to assume.
            json_loads: JSON loads function.
            json_dumps: JSON dumps function.
            speedup: If True, patch botocore with JSON functions.
        """
        self._clients: dict[tuple[str | None, str], tuple[Any, datetime | None]] = (
            dict()
        )
        if session is None:
            session = AioBoto3Session()
        self._session = session
        if config:
            config = self.DEFAULT_CONFIG.merge(config)
        self._config = config
        self._region_name = region_name
        self._role_arn = role_arn
        self._json_loads = json_loads
        self._json_dumps = json_dumps
        if speedup:
            self._patch_botocore()

    async def __aenter__(self) -> "Session":
        return self

    async def __aexit__(self, *_: Any) -> None:
        await gather(
            *(
                boto3_client.__aexit__(None, None, None)
                for boto3_client, _ in self._clients.values()
            )
        )

    async def client(
        self,
        service: "ServiceName",
        region_name: str | None = "",
        role_arn: str | None = "",
        duration: int = 3600,
        config: Optional[Config] = None,
    ) -> Any:
        """Get AWS client.

        Args:
            service: Service name.
            role_arn: Role to assume. If not specified, does not assume role.
                Explicitly pass None to enforce not using the default role.
            region_name: Region name to use. If not specified use default region.
                Explicitly pass None to enforce not using the default region.
            duration: Expiration in seconds for assumed roles.
            config: Clients config to use. If not specified, use the default config.

        Returns:
            Client
        """
        role_arn = self._role_arn if role_arn == "" else role_arn
        region_name = self._region_name if region_name == "" else region_name

        cache_key = (role_arn, service)
        try:
            cached = self._clients[cache_key]
        except KeyError:
            pass
        else:
            boto3_client = cached[0]
            expiration = cached[1]
            if expiration is None or datetime.now(timezone.utc) < expiration:
                return boto3_client
            await boto3_client.__aexit__(None, None, None)

        if not role_arn:
            boto3_client = await self._session.client(
                service, region_name=region_name
            ).__aenter__()
            expiration = None
        else:
            sts = await self.client("sts", role_arn=None, region_name=None)
            response = (
                await sts.assume_role(
                    RoleArn=role_arn,
                    RoleSessionName=gethostname(),
                    DurationSeconds=duration,
                )
            )["Credentials"]
            boto3_client = await self._session.client(
                service,
                region_name=region_name,
                config=config or self._config,
                **dict(
                    aws_access_key_id=response["AccessKeyId"],
                    aws_secret_access_key=response["SecretAccessKey"],
                    aws_session_token=response["SessionToken"],
                ),
            ).__aenter__()
            expiration = response["Expiration"] - timedelta(minutes=1)

        self._clients[cache_key] = boto3_client, expiration
        return boto3_client

    def _patch_botocore(self) -> None:
        """Patch Botocore to speed up Botocore JSON handling."""
        from botocore import serialize, parsers

        class Json:
            """JSON module."""

            loads = self._json_loads
            dumps = self._json_dumps
            JSONDecodeError = JSONDecodeError

        serialize.json = Json  # type: ignore
        parsers.json = Json  # type: ignore
