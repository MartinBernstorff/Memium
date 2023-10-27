SRC_PATH = src/personal_mnemonic_medium

install-dev:
	pip install --upgrade .[dev]

install:
	make install-dev
	pip install -e .

test: ## Run tests
	pytest tests

lint: ## Format code
	ruff format . 
	ruff . --fix \
		--extend-select F401 \
		--extend-select F841

type-check: ## Type-check code
	pyright $(SRC_PATH)

validate: ## Run all checks
	make lint
	make type-check
	make test

sync-pr:
	git push --set-upstream origin HEAD
	git push

create-pr:
	gh pr create -w || true

merge-pr:
	gh pr merge --auto --merge --delete-branch

pr: ## Run relevant tests before PR
	make sync-pr
	make create-pr
	make validate
	make merge-pr