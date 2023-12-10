import os

from latex.commands import command
from latex.common import environment


@environment("figure", indent=1)
def figure(path, centering=True, width=command("textwidth"), caption=None):
    lines = [command("includegraphics", os.path.abspath(path), width=width)]
    if centering:
        lines.append(command("centering"))
    if caption:
        lines.append(command("caption", caption))
    return "\n".join(lines)
