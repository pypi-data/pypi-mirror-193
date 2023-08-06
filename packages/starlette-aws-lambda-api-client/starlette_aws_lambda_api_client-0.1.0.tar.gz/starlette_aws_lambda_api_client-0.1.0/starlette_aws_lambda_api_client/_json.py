"""JSON speedup."""
from typing import Any as _Any, Callable as _Callable, Optional as _Optional

try:
    from orjson import dumps as _dumps, loads, JSONDecodeError
except ImportError:
    from json import loads, dumps, JSONDecodeError  # type: ignore

else:

    def dumps(  # type: ignore
        value: _Any, default: _Optional[_Callable[..., _Any]] = None, **_: _Any
    ) -> str:
        """Serialize to str JSON.

        Args:
            value: Input value.
            default: Default serializer.

        Returns:
            JSON string.
        """
        return _dumps(value, default=default).decode()


__all__ = ("dumps", "loads", "JSONDecodeError")
