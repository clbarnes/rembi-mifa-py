lint:
    uv run ruff check

lint-fix:
    uv run ruff check --fix

types:
    uv run mypy .

format:
    uv run ruff format

format-check:
    uv run ruff format --check

test:
    uv run pytest

bump BUMP: lint format-check test types
    uv sync
    test -z "$(git status --porcelain)"
    uv version --bump {{ BUMP }}
    git add -u
    git commit -m "Bump to v$(uv version | cut -d " " -f 2)"
    git tag -a "v$(uv version | cut -d " " -f 2)" -m "Version $(uv version | cut -d " " -f 2)"
