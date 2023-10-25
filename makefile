install-dev:
	pip install -r dev-requirements.txt

install-deps:
	pip install -r requirements.txt

install:
	make install-deps
	pip install -e .

test: ## Run tests
	pytest {{cookiecutter.package_name}}

lint: ## Format code
	ruff check {{cookiecutter.package_name}} --fix
	ruff format {{cookiecutter.package_name}}

type-check: ## Type-check code
	pyright {{cookiecutter.package_name}}

validate: ## Run all checks
	make lint
	make type-check
	make test

create-and-merge-pr:
	gh pr create -w || true
	gh pr merge --auto --merge --delete-branch

pr: ## Run relevant tests before PR
	make create-and-merge-pr
	make validate