from latex.commands import command
from latex.common import environment


def tabular_row(row):
    return " & ".join(str(item) for item in row) + " \\\\"


def tabular(data):

    data = data or [[]]
    format = "|" + "|".join("c" * len(data[0])) + "|"

    @environment("tabular", format, indent=1)
    def env():
        hline = command("hline")
        rows = map(lambda row: tabular_row(row), data)
        return f"\n{hline}\n" + f"\n{hline}\n".join(rows) + f"\n{hline}"

    return env
