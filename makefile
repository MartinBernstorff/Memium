install-dev:
	pip install -r dev-requirements.txt

install-deps:
	pip install -r requirements.txt

install:
	make install-deps
	pip install -e .

test: ## Run tests
	pytest src

lint: ## Format code
	ruff check src --fix
	ruff format src

type-check: ## Type-check code
	pyright src

validate: ## Run all checks
	make lint
	make type-check
	make test

create-pr:
	gh pr create -w || true

merge-pr:
	gh pr merge --auto --merge --delete-branch

pr: ## Run relevant tests before PR
	make create-pr
	make validate
	make merge-pr