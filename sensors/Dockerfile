FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.8.4 \
    POETRY_HOME="/tmp/poetry" 

WORKDIR /app

RUN apt update -y \
    && apt upgrade -y \
    && apt install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python3 \
    && python -m venv /venv

COPY . .

RUN /venv/bin/pip install --upgrade --no-cache-dir pip \
    && $POETRY_HOME/venv/bin/poetry export \
    --directory /app \
    --format requirements.txt \
    --output requirements.txt \
    --without-hashes \
    && /venv/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["/venv/bin/python", "main.py"]
