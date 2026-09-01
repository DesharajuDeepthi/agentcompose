FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY agentweave/ ./agentweave/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

EXPOSE 7777

CMD ["agentweave", "serve", "-c", "config.yaml", "--host", "0.0.0.0", "--port", "7777"]
