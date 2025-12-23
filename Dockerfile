FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

COPY main.py .

# Start HTTP server (long-running)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
