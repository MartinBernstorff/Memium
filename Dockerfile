# Builder stage
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim@sha256:fa0f9d2cf2813f3bfcdea66174039df6c181bd84b95fe32b433d14399b627c6b AS builder

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