env:
	python3 -m pip install ".[test]"

package:
	python3 -m pip install --upgrade build
	python3 -m build

test: env
	python3 -m pytest .
