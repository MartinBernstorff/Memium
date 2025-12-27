# Builder stage
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim@sha256:b34f5698ed01a8d37f11c8f9ce882caff1369cd182bd8389b04582e10f8d3e86 AS builder

ENV UV_COMPILE_BYTECODE=1
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

CMD ["uv", "run", "--no-dev", "memium"]