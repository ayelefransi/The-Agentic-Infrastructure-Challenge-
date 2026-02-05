.PHONY: setup test lint build

setup:
	pip install uv
	uv pip install --system .[dev]
	@echo "Environment setup complete."

test:
	pytest tests/

lint:
	ruff check .

build:
	docker build -t chimera-swarm .

spec-check:
	@echo "Verifying code alignment with specs..."
	# Placeholder for a script that checks if new code links to FRs
