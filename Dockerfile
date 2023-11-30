FROM python:3.12-slim

COPY src /app/src
COPY pyproject.toml /app/pyproject.toml

RUN pip install --upgrade pip \
 && cd /app \
 && pip install \
      --no-cache-dir \
      .
