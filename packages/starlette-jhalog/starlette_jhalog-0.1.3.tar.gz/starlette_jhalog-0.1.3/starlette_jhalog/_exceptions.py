"""Exceptions."""
from typing import Any, Optional, Dict
from jhalog import LogEvent
from starlette.exceptions import HTTPException as StarletteHTTPException


class HTTPException(StarletteHTTPException):
    """Starlette "HTTPException" with extra "error_detail" field."""

    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
        *,
        error_detail: Optional[Any] = None,
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        LogEvent.set_to_context(error_detail=error_detail or detail)
