deploy:
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile
	cd /Users/martinbernstorff/Git/dotfiles/containers/memium && docker compose down && docker compose up -d

validate:
	make test

test:
	uv run pyright
	uv run pytest

snapshot:
	uv run pytest --inline-snapshot=review