"""Invoke Helpers."""

import platform
from contextlib import suppress
from functools import lru_cache
from os import environ

from beartype import beartype
from beartype.typing import Any
from invoke import Context, Result


@lru_cache(maxsize=1)
@beartype
def use_pty() -> bool:
    """Returns False on Windows and some CI environments."""
    if platform.system() == 'Windows':
        return False
    return not environ.get('GITHUB_ACTION')


@beartype
def run(ctx: Context, *run_args: Any, **run_kwargs: Any) -> Result:
    """Wrap invoke.run to run within the `working_dir`."""
    working_dir = '.'
    with suppress(AttributeError):
        working_dir = ctx.config.gto.working_dir

    with ctx.cd(working_dir):
        return ctx.run(*run_args, **run_kwargs)
