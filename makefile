deploy:
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile
	cd /Users/martinbernstorff/Git/dotfiles/containers/memium && docker compose down && docker compose up -d

validate:
	make test

verify:
	uv run pyright
	uv run pytest --durations=5
	make vulture

snapshot:
	uv run pytest --inline-snapshot=review

deploy:
	make verify
	make build
	cd $(DOCKER_COMPOSE_DIR) && docker compose down && docker compose up -d

vulture:
	uv run vulture memium vulture_whitelist.py --exclude "test_*.py" --min-confidence 100 --sort-by-size
