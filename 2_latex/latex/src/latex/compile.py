import tempfile
import shutil
import subprocess
import os


def compile(doc, path):

    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "source.tex"), "w") as fp:
            fp.write(doc)

        subprocess.call(["pdflatex", "source.tex", "-o", "source.pdf"], cwd=tmpdir)

        shutil.copyfile(os.path.join(tmpdir, "source.pdf"), path)
