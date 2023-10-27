# Use an official Python runtime as a parent image
FROM python:3.11-bookworm

# Set the working directory to /app
WORKDIR /app
RUN pip install pyright
RUN pyright .

# Install deps
COPY pyproject.toml ./
RUN pip install --upgrade .[dev]
RUN pip install --upgrade .[tests]

# Ensure pyright builds correctly. 
# If run in make validate, it is run in parallel, which breaks its installation.
# Install the entire app
COPY . /app
RUN pip install -e .
