"""Extend Invoke for Calcipy."""

import os
import sys
from pathlib import Path

from beartype.typing import Any, Callable, Dict
from beartype import beartype
from beartype.typing import List
from invoke import Task, Collection, Config, Context, Program
from functools import wraps
from contextlib import suppress
import logging
from .log import configure_logger
from invoke import task as invoke_task
from pydantic import BaseModel, Field, PositiveInt, conint
from .log import get_logger
from .invoke_helpers import use_pty

logger = get_logger()


class GlobalTaskOptions(BaseModel):
    """Global Task Options."""

    working_dir: Path = Field(default_factory=Path.cwd)
    """Working directory for the program to use globally."""

    file_args: List[Path] = Field(default_factory=list)
    """List of Paths to modify."""

    verbose: PositiveInt = Field(default=2, lte=3)
    """Verbosity level."""


class _ShoalProgram(Program):
    """Customized version of Invoke's `Program`."""

    def print_help(self) -> None:
        """Extend print_help with shoal-specific global configuration.

        https://github.com/pyinvoke/invoke/blob/0bcee75e4a26ad33b13831719c00340ca12af2f0/invoke/program.py#L657-L667

        """
        super().print_help()
        print('Global Task Options:')  # noqa: T201
        print('')  # noqa: T201
        self.print_columns([
            ('working_dir', 'Set the cwd for the program. Example: "../run --working-dir .. lint test"'),
            ('*file_args', 'List of Paths available globally to all tasks. Will resolve paths with working_dir'),
            ('verbose', 'Globally configure logger verbosity (-vvv for most verbose)'),
        ])
        print('')  # noqa: T201

class ShoalConfig(Config):

    @staticmethod
    def global_defaults() -> Dict:
        """Override the global defaults."""
        defaults = Config.global_defaults()
        return {
            **defaults,
            "run": {
                **defaults["run"],
                "asynchronous": False,  # PLANNED: When can this be True?
                "echo": True,
                "echo_format": "\033[2;3;37mRunning: {command}\033[0m",
                "pty": use_pty(),
            },
        }

@beartype
def start_program(pkg_name: str, pkg_version: str, module) -> None:
    """Run the customized Invoke Program.

    FYI: recommendation is to extend the `core_args` method, but this won't parse positional arguments:
    https://docs.pyinvoke.org/en/stable/concepts/library.html#modifying-core-parser-arguments

    """
    # Manipulate 'sys.argv' to hide arguments that invoke can't parse
    _gto = GlobalTaskOptions()
    sys_argv: List[str] = []
    last_argv = ''
    for argv in sys.argv:
        if not last_argv.startswith('-') and Path(argv).is_file():
            _gto.file_args.append(Path(argv))
        elif argv in {'-v', '-vv', '-vvv', '--verbose'}:
            _gto.verbose = argv.count('v')
        elif last_argv in {'--working-dir',}:
            _gto.working_dir = Path(argv).resolve()
        elif argv not in {'--working-dir',}:
            sys_argv.append(argv)
        last_argv = argv
    _gto.file_args = [
        _f if _f.is_absolute() else Path.cwd() / _f
        for _f in _gto.file_args
    ]
    sys.argv = sys_argv

    class _ShoalConfig(ShoalConfig):

        gto: GlobalTaskOptions = _gto

    _ShoalProgram(
        name=pkg_name,
        version=pkg_version,
        namespace=Collection.from_module(module),
        config_class=_ShoalConfig,
    ).run()


@beartype
def task(*task_args, **task_kwargs) -> Callable[[Any], Task]:
    """Wrapper to accept arguments for an invoke task."""
    @beartype
    def wrapper(func) -> Task:
        """Wraps the decorated task."""
        @invoke_task(*task_args, **task_kwargs)
        @beartype
        @wraps(func)
        def inner(ctx: Context, *args, **kwargs) -> Task:
            """Wrap the task with settings configured in `gto` for working_dir and logging."""
            try:
                ctx.config.gto
            except AttributeError:
                ctx.config.gto = GlobalTaskOptions()

            os.chdir(ctx.config.gto.working_dir)

            verbose = ctx.config.gto.verbose
            log_lookup = {3: logging.NOTSET, 2: logging.DEBUG, 1: logging.INFO, 0: logging.WARNING}
            raw_log_level = log_lookup.get(verbose)
            configure_logger(log_level=logging.ERROR if raw_log_level is None else raw_log_level)

            summary = func.__doc__.split('\n')[0]
            logger.print(f'Running {func.__name__}', is_header=True, summary=summary)
            logger.print_debug('With task arguments', args=args, kwargs=kwargs)

            result = func(ctx, *args, **kwargs)

            logger.print_debug(f'Completed {func.__name__}', result=result)
            return result
        return inner
    return wrapper
