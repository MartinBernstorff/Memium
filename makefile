deploy:
	make validate
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile
	cd /Users/martinbernstorff/Git/dotfiles/containers/memium && docker compose down && docker compose up -d

verify:
	make types
	make test
	make vulture

validate:
	make verify

types:
	uv run pyright

test:
	uv run pytest --durations=5


snapshot:
	uv run pytest --inline-snapshot=review

vulture:
	uv run vulture memium vulture_whitelist.py --exclude "test_*.py" --min-confidence 100 --sort-by-size
