import functools

import latex.commands as cmd


def _tabulate(n_tabs, text):
    return ("\t" * n_tabs).join(("\n" + text.lstrip()).splitlines(True))[1:]


def environment(name, *env_args, indent=0):
    def inner(gen):
        @functools.wraps(gen)
        def wrapper(*args, **kwargs):
            res = cmd.begin(name, *env_args)
            res += "\n" + _tabulate(indent, gen(*args, **kwargs)) + "\n"
            res += cmd.end(name)
            return res
        return wrapper
    return inner


center = functools.partial(environment, "center")
