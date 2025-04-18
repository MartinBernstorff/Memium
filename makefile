build:
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile

test:
	uv run pyright
	uv run pytest

snapshot:
	uv run pytest --inline-snapshot=review