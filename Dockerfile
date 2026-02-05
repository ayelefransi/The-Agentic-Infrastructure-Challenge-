FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    start-stop-daemon \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install build tools
RUN pip install --no-cache-dir uv

# Copy project definition
COPY pyproject.toml .

# Install dependencies
RUN uv pip install --system . --optional dev

# Copy code
COPY . .

# Default command (can be overridden)
CMD ["python", "-m", "chimera.orchestrator"]
