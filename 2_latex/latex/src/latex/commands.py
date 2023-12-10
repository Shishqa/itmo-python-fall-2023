import functools


def command(name, *args, **kwargs):
    chunks = [f"\\{name}"]
    if len(kwargs) > 0:
        chunks.append("[" + ",".join(f"{key}={value}" for key, value in kwargs.items()) + "]")
    chunks.append("".join(f"{{{arg}}}" for arg in args))
    return "".join(chunks)


begin = functools.partial(command, "begin")
end = functools.partial(command, "end")
documentclass = functools.partial(command, "documentclass")
