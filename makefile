SRC_PATH = personal_mnemonic_medium
MAKEFLAGS = --no-print-directory

# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/205 Decrease makefile verbosity
# E.g. entering/leaving directory
# Or showing each command when running make pr

deploy:
	./docker_cmd.sh

install-test:
	@pip install --upgrade .[dev,tests]

install-dev:
	@pip install --upgrade .[dev]

install:
	@make install-dev
	@pip install -e .

test: ## Run tests with coverage
	# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/209 Fix coverage and add it to make pr
	@echo "––– Testing –––"
	@pytest --cov=personal_mnemonic_medium personal_mnemonic_medium --cov-report=xml
	@diff-cover coverage.xml
	@echo "✅✅✅ Tests passed ✅✅✅"

lint: ## Format code
	@echo "––– Linting –––"
	@ruff format . 
	@ruff . --fix \
		--extend-select F401 \
		--extend-select F841
	@echo "✅✅✅ Lint ✅✅✅"

types: ## Type-check code
	@echo "––– Type-checking –––"
	@pyright $(SRC_PATH)
	@echo "✅✅✅ Types ✅✅✅"

validate: ## Run all checks
	@echo "––– Running all checks –––"
	@make lint
	@make types
	@make test

merge-main:
	@echo "––– Merging main –––"
	@git fetch
	@git merge --no-edit origin/main

mm:
	@make merge-main

push:
	@echo "––– Pushing to origin/main –––"
	@git push --set-upstream origin HEAD
	@git push

create-pr:
	@echo "––– Creating PR –––"
	@gh pr create --title "$$(git log -1 --pretty=%B)" --body "Auto-created" || true

enable-automerge:
	@gh pr merge --auto --squash --delete-branch

squash-from-parent:
	@git fetch
	@git reset $$(git merge-base origin/main $$(git rev-parse --abbrev-ref HEAD)) ; git add -A ; git commit -m "Squash changes from parent branch"

create-random-branch:
	@git checkout -b "$$(date +'%d_%H_%M')_$(shell cat /dev/urandom | env LC_ALL=C tr -dc 'a-z' | fold -w 5 | head -n 1)"

pr-status:
	@gh pr view | cat | grep "title" 
	@gh pr view | cat | grep "url" 
	@echo "✅✅✅ PR created ✅✅✅"

setup-pr: ## Update everything and setup the PR
	@make merge-main
	@make push
	@make create-pr
	@make enable-automerge

pr: ## Run relevant tests before PR
	@make merge-main
	@make push
	@make create-pr
	@make validate
	@make enable-automerge
	@echo "––– 🎉🎉🎉 All validation succeeded! 🎉🎉🎉 –––"
	@make pr-status

grow:
	@make pr
	@echo "––– Growing into a new branch 🌳 –––"
	@make create-random-branch
	@make squash-from-parent