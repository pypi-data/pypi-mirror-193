"""Jhalog (JSON HTTP Access Log) middleware for Starlette/FastAPI."""
from asyncio import wait_for as _wait_for
from typing import Awaitable as _Awaitable, Any as _Any, Callable as _Callable
from jhalog import AsyncLogger as _AsyncLogger, LogEvent as _LogEvent
from starlette.middleware.base import BaseHTTPMiddleware as _BaseHTTPMiddleware
from starlette.applications import Starlette as _Starlette
from starlette.requests import Request as _Request
from starlette.responses import (
    Response as _Response,
    PlainTextResponse as _PlainTextResponse,
)
from starlette.status import (
    HTTP_500_INTERNAL_SERVER_ERROR as _HTTP_500_INTERNAL_SERVER_ERROR,
)


class JalogMiddleware:
    """Jhalog Middleware.

    Args:
        app: Starlette/FastAPI Application.
        backend: Backend to use.
        backend_config: Backend configuration.
        request_timeout: Request timeout in seconds. 0 to disable timeout.
            Raises 504 HTTP error is reached. Default to 50 seconds (less to the default
            60s values used in most load balancers and reverse proxies to ensure the
            504 error is risen by the server en properly logged).
        ignore_paths: Paths to do not log.
        forward_request_id: If Set to True, forward the request "X-request-ID"
            header to the "request_id" log event field and the "X-request-ID" response
            header. A random value is generated if this option is False
            or if the request does not contain the "X-request-ID" header.
        kwargs: Extra jhalog.Logger parameters, like _backends specific parameters.
    """

    __slots__ = ["_logger", "_request_timeout", "_forward_request_id"]

    def __init__(
        self,
        app: _Starlette,
        backend: str,
        *,
        request_timeout: int = 50,
        forward_request_id: bool = True,
        **kwargs: _Any
    ) -> None:
        self._request_timeout = request_timeout if request_timeout > 0 else None
        self._logger = _AsyncLogger(backend=backend, exception_hook=True, **kwargs)
        self._forward_request_id = forward_request_id

        app.router.on_startup.insert(0, self._logger.__aenter__)
        app.add_event_handler("startup", self._logger.emit_startup_completed_event)
        app.add_event_handler("shutdown", self._logger.__aexit__)
        app.add_middleware(_BaseHTTPMiddleware, dispatch=self._middleware_dispatch)
        app.add_exception_handler(Exception, self._server_error_response)

    async def _middleware_dispatch(
        self, request: _Request, call_next: _Callable[[_Request], _Awaitable[_Response]]
    ) -> _Response:
        """HTTP Middleware dispatch function.

        Args:
            request: Request.
            call_next: Returns response based on request.

        Returns:
            Response.
        """
        with self._logger.create_event(
            method=request.method,
            path=request.url.path,
            user_agent=request.headers.get("User-Agent"),
            request_id=(
                request.headers.get("X-request-ID")
                if self._forward_request_id
                else None
            ),
        ) as event:
            try:
                event.client_ip = request.scope["client"][0]
            except TypeError:
                pass

            try:
                response = await _wait_for(call_next(request), self._request_timeout)

            except Exception as exc:
                status, message = event.status_code_from_exception(exc)
                if status == _HTTP_500_INTERNAL_SERVER_ERROR:
                    raise
                return _PlainTextResponse(
                    message, status, {"X-request-ID": event.request_id}
                )

            response.headers["X-request-ID"] = event.request_id
            event.status_code = response.status_code
            return response

    @staticmethod
    async def _server_error_response(*_: _Any) -> _Response:
        """Return internal server error.

        Returns:
            Response.
        """
        return _PlainTextResponse(
            "Internal Server Error",
            status_code=_HTTP_500_INTERNAL_SERVER_ERROR,
            headers={"X-request-ID": _LogEvent.from_context().request_id},
        )
