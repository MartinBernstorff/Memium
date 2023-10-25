lint:
	@echo Running black
	black .

	@echo Running ruff
	ruff check . --fix

test:
	@echo ––– Testing –––
	pytest -n auto -rfE --failed-first --disable-warnings -q

type-check:
	@echo ––– Running static type checks –––
	pyright .

install:
	pip install --upgrade -e .[dev,tests]

validate:
	@echo ––– Ensuring dependencies are up to date. This will take a few moments ---
	@make install > /dev/null
	@make lint && make type-check && make test

pr:
	gh pr create
	make validate
	git push
	gh pr merge --auto --merge