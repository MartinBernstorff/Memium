FROM python:3.11-bookworm as builder
WORKDIR /app

# Install build utilities and python requirements
COPY pyproject.toml ./
RUN pip install --user --no-cache-dir .
COPY ./ ./

# Stage 2: Production
FROM python:3.11-slim-bookworm
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:${PATH}
COPY --from=builder /app .