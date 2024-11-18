# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install necessary system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Flask
RUN pip install flask

# Expose the backend port
EXPOSE 3000

# Default command to keep the container running, overridden in the Deployment
CMD ["tail", "-f", "/dev/null"]
