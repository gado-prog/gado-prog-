# 🚀 Deploy

## Local

```bash
pip install -r requirements.txt
python run_demo.py
```

Open `http://127.0.0.1:8000` or `/docs`.

## Docker

```bash
docker compose up --build
```

## Online deployment

The repository includes `render.yaml` and a Dockerfile. On Render, create a new Blueprint from this repository; Render reads `render.yaml`, builds the Docker image and uses `/health` for health checks.

## Environment

Copy `.env.example` to `.env` locally. Never commit real API keys. Production secrets should be stored in the hosting provider's secret/environment settings.
