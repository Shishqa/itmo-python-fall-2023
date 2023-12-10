from latex.document import document
from latex.tabular import tabular
from latex.common import center
from latex.compile import compile
from latex_img.figure import figure


@document("article")
def my_document_with_table():
    data = [
        ["id", "name"],
        [1, "Nick"],
        [2, "Bobby"],
        [3, "Tom"],
    ]
    return center()(tabular(data))()


@document("article", packages=["graphicx"])
def my_document_with_puppy():
    figure_path = "artifacts/puppy.jpg"
    return figure(figure_path, caption="My lovely puppy")


def render_and_compile(doc, name):
    with open(f"artifacts/{name}.tex", "w") as fp:
        fp.write(doc)
    compile(doc, f"artifacts/{name}.pdf")


if __name__ == "__main__":
    render_and_compile(my_document_with_table(), "1")
    render_and_compile(my_document_with_puppy(), "2")
