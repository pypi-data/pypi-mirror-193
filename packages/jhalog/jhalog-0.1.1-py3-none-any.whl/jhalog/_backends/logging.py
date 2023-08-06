"""Standard library logger."""
from __future__ import annotations
from logging import Logger as StdlibLogger, getLogger
from typing import Any
from jhalog._base import LoggerBase
from jhalog._event import LogEvent


class Logger(LoggerBase):
    """Standard library logger."""

    __slots__ = ("_logger",)

    def __init__(self, logger: StdlibLogger | None = None, **kwargs: Any) -> None:
        LoggerBase.__init__(self, **kwargs)
        self._logger = logger or getLogger()

    def _emit(self, event: LogEvent) -> None:
        """Emit log event.

        Args:
            event: Log event.
        """
        self._emit_stdlib_logger(self._logger, event)
