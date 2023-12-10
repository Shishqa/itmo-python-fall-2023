import os
from latex.document import document

from latex_img.figure import figure
import pytest


@pytest.fixture
def test_document():

    @document("article")
    def my_document():
        figure_path = "puppy.jpg"
        return figure(figure_path, caption="My lovely puppy")

    return my_document


def test_document_with_figure(test_document):
    latex_code = test_document()
    assert latex_code == f"""\\documentclass{{article}}
\\begin{{document}}
\\begin{{figure}}
\t\\includegraphics{{{os.getcwd()}/puppy.jpg}}
\t\\centering
\t\\caption{{My lovely puppy}}
\\end{{figure}}
\\end{{document}}"""
