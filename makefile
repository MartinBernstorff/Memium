info:
	@echo "\nThis project uses invoke. \nInstall it using "pip install invoke"\nRun invoke --list to see available commands.\n\n"

build:
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile

test:
	uv run pyright
	uv run pytest

snapshot:
	uv run pytest --inline-snapshot=review