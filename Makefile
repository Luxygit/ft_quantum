EX = superposition.py

all: install run

install:
	uv sync

run: install
	uv run python -m src $(EX)

debug: install
	uv run python -m pdb src $(EX)

clean:
	rm -rf .mypy_cache dist build *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +

lint:
	uv run flake8 src/ft_quantum/
	uv run mypy src/ft_quantum --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run flake8 .
	uv run mypy . --strict

.PHONY: all install run debug clean lint lint-strict
