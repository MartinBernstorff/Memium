lint:
	pre-commit run --all-files

test:
	pytest -n auto -rfE --failed-first --disable-warnings -q

pr:
	make lint & make test
	gh pr create
	gh pr merge --auto --merge