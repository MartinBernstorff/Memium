# Variables
VENV           = .venv
VENV_PYTHON    = $(VENV)/bin/python
SYSTEM_PYTHON  = $(or $(shell which python3.9), $(shell which python3))
PYTHON         = $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))

.DEFAULT_GOAL := help
.PHONY: coverage deps help lint publish push test tox

setup:
	@$(MAKE) git_init
	@$(MAKE) setup_venv
	@$(MAKE) install

git_init:
	@if [ ! -d ".git" ]; then \
        echo "🔨 Initializing Git repository..."; \
        git init; \
		git add.; \
		git commit -m "Initial commit"; \
		@echo "✅ Git repository initialized"; \
    else \
        @echo "✅ Git repository already exists, continuing"; \
    fi

setup_venv:
	@if [ ! -d ".venv" ]; then \
        @echo "🔨 Creating virtual environment with $(SYSTEM_PYTHON)..."; \
        $(SYSTEM_PYTHON) -m venv .venv; \
		@echo "✅ Virtual environment created"; \
    else \
        @echo "✅ Virtual environment already exists, continuing"; \
    fi

install: ## Install the project as editable, ready for dev
	@echo 🔨 Installing project... \ 
	$(PYTHON) -m pip install -e ".[dev,tests]"; \

update: ## Update dependencies
	@echo 🔨 Updating project... \
	$(PYTHON) -m pip install --upgrade -e ".[dev,tests]" \

test:
	@pytest -x -n 4 -rfE -p no:typeguard -p no:cov

lint: ## Lint and static check
	@$(MAKE) pre_commit
	@$(MAKE) mypy

pr: ## Create a PR, then run linting and tests
	@$(MAKE) lint
	@$(MAKE) test
	
	@if [ `gh pr list | wc -l` -gt 0 ]; then \
		echo "✈️ Pushing to existing PR..."; \
		git push; \
	else \
		gh pr create --web; \
	fi

	@echo "✅ PR up-to-date!"

mypy:
	@echo "\n––– 🧹 Running mypy –––"
	@$(PYTHON) -m mypy .

pre_commit: 
	@echo "\n––– 🧹 Running pre-commit checks –––"
	@pre-commit run --all-files

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done