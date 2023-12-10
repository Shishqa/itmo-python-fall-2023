import functools


def command(name, *args):
    formatted_args = "".join(f"{{{arg}}}" for arg in args)
    return f"\\{name}{formatted_args}"


begin = functools.partial(command, "begin")
end = functools.partial(command, "end")
documentclass = functools.partial(command, "documentclass")
