build:
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile

validate:
	make test

test:
	uv run pyright
	uv run pytest

snapshot:
	uv run pytest --inline-snapshot=review