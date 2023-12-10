import pytest

from latex.tabular import tabular
from latex.document import document
from latex.common import center


@pytest.fixture
def test_document():

    @document("article")
    def my_document():
        data = [
            ["id", "name"],
            [1, "Nick"],
            [2, "Bobby"],
            [3, "Tom"],
        ]
        return center()(tabular(data))()

    return my_document


def test_document_full(test_document):
    latex_code = test_document()
    assert latex_code == """\\documentclass{article}
\\begin{document}
\\begin{center}
\\begin{tabular}{c c}
\tid & name \\\\
\t1 & Nick \\\\
\t2 & Bobby \\\\
\t3 & Tom \\\\
\\end{tabular}
\\end{center}
\\end{document}"""
