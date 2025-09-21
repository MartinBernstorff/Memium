build:
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile

validate:
	uv run pyright
	uv run pytest
	make vulture

snapshot:
	uv run pytest --inline-snapshot=review

deploy:
	make build
	cd $(DOCKER_COMPOSE_DIR) && docker compose down && docker compose up -d

vulture:
	uv run vulture memium vulture_whitelist.py --exclude "test_*.py"
