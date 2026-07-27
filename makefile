deploy:
	make deploy-life-lessons
	make deploy-flowbase

deploy-life-lessons:
	docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile
	cd ~/Git/dotfiles/containers/memium && docker compose down && docker compose up -d
	@echo "✅ Deploy succeeded!"

deploy-flowbase:
	docker build . -t ghcr.io/martinbernstorff/flowbase:latest -f Dockerfile
	cd ~/Git/dotfiles/containers/memium-flowbase && docker compose down && docker compose up -d
	@echo "✅ Deploy succeeded!"

verify:
	make types
	make test
	make vulture
	@echo "✅ Verify succeeded!"

validate:
	make verify
	@echo "✅ Validate succeeded!"

types:
	uv run pyright
	@echo "✅ Types check succeeded!"

test:
	uv run pytest --durations=5
	@echo "✅ Tests succeeded!"

snapshot:
	uv run pytest --inline-snapshot=review
	@echo "✅ Snapshot tests succeeded!"

vulture:
	uv run vulture memium vulture_whitelist.py --exclude "test_*.py" --min-confidence 100 --sort-by-size
	@echo "✅ Vulture check succeeded!"
