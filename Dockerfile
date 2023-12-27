FROM python:3.12-bookworm as builder
WORKDIR /app

# Install build utilities and python requirements
COPY pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/pip pip install --user . --no-compile
COPY ./ ./

# Stage 2: Production
FROM python:3.12-slim-bookworm
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:${PATH}
COPY --from=builder /app .
RUN pip install .
ENV ENV=production-container