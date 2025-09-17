build:
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile

test:
	uv run pyright
	uv run pytest

deploy:
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile

snapshot:
	uv run pytest --inline-snapshot=review