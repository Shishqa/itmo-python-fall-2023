import functools

import latex.commands as cmd
from latex.common import environment


def document(kind):
    def inner(gen):
        @functools.wraps(gen)
        def wrapper(*args, **kwargs):
            res = cmd.documentclass(kind) + "\n"
            res += environment("document")(gen)(*args, **kwargs)
            return res
        return wrapper
    return inner
