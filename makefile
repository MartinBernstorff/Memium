SRC_PATH = personal_mnemonic_medium

deploy:
	./docker_cmd.sh

install-dev:
	pip install --upgrade .[dev]

install:
	make install-dev
	pip install -e .

test: ## Run tests
	pytest personal_mnemonic_medium/tests

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

merge-main:
	git fetch
	git merge --no-edit origin/main

push:
	git push --set-upstream origin HEAD
	git push

create-pr:
	gh pr create --title "$$(git log -1 --pretty=%B)" --body "Auto-created" || true

enable-automerge:
	gh pr merge --auto --squash --delete-branch

squash-from-parent:
	git fetch
	git reset $$(git merge-base origin/main $$(git rev-parse --abbrev-ref HEAD)) ; git add -A ; git commit -m "Squash changes from parent branch"

create-random-branch:
	@git checkout -b "$$(date +'%d_%H_%M')_$(shell cat /dev/urandom | env LC_ALL=C tr -dc 'a-z' | fold -w 5 | head -n 1)"

pr-status:
	@gh pr view | cat | grep "title" 
	@gh pr view | cat | grep "url" 

pr: ## Run relevant tests before PR
	@make push
	@make create-pr
	@make merge-main
	@make validate
	@make enable-automerge
	@echo "––– 🎉🎉🎉 All tests succeeded! 🎉🎉🎉 –––"
	@make pr-status

grow:
	make pr
	@echo "––– Growing into a new branch 🌳 –––"
	make create-random-branch
	make squash-from-parent