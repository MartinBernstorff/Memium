# Builder stage
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim@sha256:2d0d1ddd438eda34e0604caa30ff313a2521aab6290d3c49e1ce661fa63a2c48 AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


# Runner stage
FROM python:3.14-slim@sha256:e93b62290efbb6207b8d23355c25f61a04fa100323727fe5e6b052d5f01d6788 AS runner
WORKDIR /app
RUN useradd -m appuser
COPY --from=builder --chown=app:app /app /app
ENV PATH="/app/.venv/bin:$PATH"
ENV ENV="prod-container"

USER appuser