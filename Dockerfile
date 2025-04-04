# Use an official Python base image
FROM python:3.11-slim

# Install curl (to download ngrok) and other dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Download ngrok
RUN curl -s https://ngrok.com/download | tar xz && mv ngrok /usr/local/bin/ngrok

# Verify installation
RUN ngrok version

# Default command (can be overridden)
CMD ["python3"]
