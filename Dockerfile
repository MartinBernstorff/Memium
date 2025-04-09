# Builder stage
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim@sha256:6ca00262f16f5296f1c0a8b3ac6616c1ab933ba02d90d2c2d1e846db4d788b00 AS builder

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
FROM python:3.11-slim@sha256:80bcf8d243a0d763a7759d6b99e5bf89af1869135546698be4bf7ff6c3f98a59 AS runner
WORKDIR /app
RUN useradd -m appuser
COPY --from=builder --chown=app:app /app /app
ENV PATH="/app/.venv/bin:$PATH"
ENV ENV="prod-container"

USER appuser