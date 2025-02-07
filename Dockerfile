FROM docker.io/library/python:3.12-bookworm@sha256:99bb27b18fc0b930cdc372f9e17fe4b0c2a50686504c8ed8aa32397acbad603b as builder
WORKDIR /app

# Install build utilities and python requirements
COPY pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/pip pip install --user . --no-compile
COPY ./ ./

# Stage 2: Production
FROM docker.io/library/python:3.12-bookworm@sha256:99bb27b18fc0b930cdc372f9e17fe4b0c2a50686504c8ed8aa32397acbad603b
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:${PATH}
COPY --from=builder /app .
RUN pip install .
ENV ENV=production-container