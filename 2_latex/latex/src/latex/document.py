import functools

import latex.commands as cmd
from latex.common import environment


def document(kind, packages=None):
    packages = packages or []
    def inner(gen):
        @functools.wraps(gen)
        def wrapper(*args, **kwargs):
            lines = [cmd.documentclass(kind)]
            for package in packages:
                lines.append(cmd.command("usepackage", package))
            lines.append(environment("document")(gen)(*args, **kwargs))
            return "\n".join(lines)
        return wrapper
    return inner
