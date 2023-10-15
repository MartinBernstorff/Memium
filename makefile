lint:
	pre-commit run --all-files

test:
	pytest -n auto -rfE --failed-first --disable-warnings -q

type-check:
	pyright .

validate:
	make lint & make test & make type-check

pr:
	make validate
	git push
	gh pr create
	gh pr merge --auto --merge