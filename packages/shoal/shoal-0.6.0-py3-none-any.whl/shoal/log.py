"""Log."""

from datetime import datetime
import logging
from functools import cached_property, partial

from beartype import beartype
from beartype.typing import Any, Callable, Dict, Optional
from pydantic import BaseModel
from rich.console import Console
from rich.text import Text

_DEF_LEVEL = logging.ERROR


class _Styles:
    """Based on `tail-jsonl`."""

    timestamp: str = 'dim grey'
    message: str = ''

    level_error: str = 'red'
    level_warn: str = 'yellow'
    level_info: str = 'green'
    level_debug: str = 'dim blue'

    key: str = 'bold blue'
    value: str = ''

    @cached_property
    def _level_lookup(self) -> Dict[int, str]:
        return {
            logging.CRITICAL: self.level_error,
            logging.ERROR: self.level_error,
            logging.WARNING: self.level_warn,
            logging.INFO: self.level_info,
            logging.DEBUG: self.level_debug,
        }

_LEVEL_TO_NAME = {
    logging.CRITICAL: "EXCEPTION",
    logging.ERROR: "ERROR",
    logging.WARNING: "WARNING",
    logging.INFO: "INFO",
    logging.DEBUG: "DEBUG",
    logging.NOTSET: "NOTSET",
}
"""Mapping to logging level name.

https://docs.python.org/3.11/library/logging.html#logging-levels

"""

_STYLES = _Styles()


@beartype
def _log(
    message,
    *,
    _log_level: int, _this_level: int, _console: Console,
    is_print: bool = False, is_header: bool = False,
    **kwargs,
) -> None:
    """Default log function."""
    if _this_level < _log_level:
        return

    text = Text()
    if is_print:
        mesage_style = ('bold ' if is_header else '') + _STYLES.level_info
        text.append(f"{message}", style=mesage_style)
    else:
        text.append(f"{datetime.now()} ", style=_STYLES.timestamp)
        text.append(_LEVEL_TO_NAME.get(_this_level, ''), style=_STYLES._level_lookup.get(_this_level))
        text.append(f" {message}", style=_STYLES.message)
    for key, value in kwargs.items():
        text.append(f' {key}:', style=_STYLES.key)
        text.append(f' {str(value): <10}', style=_STYLES.value)
    _console.print(text)

    if _this_level == logging.CRITICAL:
        _console.print_exception(show_locals=True)
        # # Or:
        # from rich.traceback import install
        # install(show_locals=True)


class _LogSingleton(BaseModel):
    """Store pointer to log function."""

    log: Callable[[Any], None]


_LOG_SINGLETON = _LogSingleton(log=partial(_log, _log_level=_DEF_LEVEL, _console=Console()))


class _Logger:

    @beartype
    def print(self, message, is_header: bool = False, **kwargs) -> None:
        """Print the content without a leading timestamp.

        If writing to a file or not natively supported by the logger, will appear in the logs as level info.

        """
        self.info(message, **{'is_print': True, 'is_header': is_header, **kwargs})

    @beartype
    def print_debug(self, message, is_header: bool = False, **kwargs) -> None:
        """Variation on print that will appear as a debug log if not supported."""
        self.debug(message, **{'is_print': True, 'is_header': is_header, **kwargs})

    @beartype
    def debug(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.DEBUG, **kwargs)

    @beartype
    def info(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.INFO, **kwargs)

    @beartype
    def warning(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.WARNING, **kwargs)

    @beartype
    def error(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.ERROR, **kwargs)

    @beartype
    def exception(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.CRITICAL, **kwargs)


@beartype
def configure_logger(log_level: int = _DEF_LEVEL) -> None:
    """Configure global logger."""
    _LOG_SINGLETON.log = partial(_log, _log_level=log_level, _console=Console())


@beartype
def get_logger() -> _Logger:
    """Retrieve global logger."""
    return _Logger()
