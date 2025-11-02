FROM python:3.11-slim
WORKDIR /app

# chromadb sometimes needs build tools / system libs
RUN apt-get update && apt-get install -y build-essential git libgl1 && rm -rf /var/lib/apt/lists/*

COPY services/mcp_vector/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY services/mcp_vector/src /app/src
CMD ["python", "src/server.py"]
