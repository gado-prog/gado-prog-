# 📈 ML Observability Platform

Monitoring and evaluation layer for AI/ML services. The goal is to make model quality measurable instead of treating AI as a black box.

## Signals

- Request latency and error rate
- Token/cost metadata when available
- Retrieval quality metrics
- Evaluation scores
- Model/version tracking
- Regression alerts

## Architecture

`AI API → Events → Metrics Store → Evaluation Jobs → Dashboard/Alerts`

## Stack

Python · FastAPI · PostgreSQL · metrics · GitHub Actions
