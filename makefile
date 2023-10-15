lint:
	pre-commit run --all-files

test:
	pytest -n auto -rfE --failed-first --disable-warnings -q

type-check:
	pyright .

validate:
	make install
	make lint & make test & make type-check

install:
	pip install --upgrade -e .[dev,test]

pr:
	make validate
	git push
	gh pr create
	gh pr merge --auto --merge