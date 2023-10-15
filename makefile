lint:
	pre-commit run --all-files

test:
	pytest -n auto -rfE --failed-first --disable-warnings -q

type-check:
	pyright .

pr:
	make lint & make test & make type-check
	gh pr create
	gh pr merge --auto --merge