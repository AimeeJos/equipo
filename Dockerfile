FROM python:3.10-slim

LABEL maintainer="learnaimee@gmail.com"

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Copy requirements files and application code
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

# Set working directory
WORKDIR /app

# Expose port 8000
EXPOSE 8000

# Set a build argument for the development environment
ARG DEV=false

# Install system dependencies and Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && /py/bin/pip install -r /tmp/requirements.txt \
    && if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt ; fi \
    && rm -rf /tmp

# Create a non-root user
RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user \
    && mkdir -p /vol/web/media \
    && mkdir -p /vol/web/static \
    && chown -R django-user:django-user /vol

# Set PATH environment variable
ENV PATH="/py/bin:${PATH}"

# Switch to non-root user
USER django-user