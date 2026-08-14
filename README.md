# 👋 Gado — AI / Python Engineer Portfolio

> **Working AI products, not README-only demos.**

## 🚀 Live-capable portfolio

This repository contains runnable AI/ML prototypes, APIs, browser demos, automated tests, Docker infrastructure and deployment configuration.

| Project | Focus | Status |
|---|---|---|
| 🧠 Autonomous Research Agent | Agent workflows / RAG | Runnable API foundation |
| 📚 Multimodal Knowledge Copilot | RAG / OCR / retrieval | Runnable API foundation |
| 🏢 AI Customer Operations Agent | Support automation | Runnable API |
| 🎥 Football Intelligence Platform | CV / tracking | Runnable API foundation |
| 🎙️ Voice AI Assistant | ASR / TTS architecture | Runnable API foundation |
| 📈 ML Observability Platform | MLOps / metrics | Runnable API |
| ⚽ Football AI Analyzer | YOLO / video CV | Runnable API foundation |
| 🤖 AI Document Assistant | Document RAG | Runnable API foundation |
| 👁️ Computer Vision Toolkit | OpenCV | Runnable utility + tests |
| 🚀 ML API Starter | Model serving | Runnable API |

## ⚡ Run it

### Python

```bash
pip install -r requirements.txt
python run_demo.py
```

Open **http://127.0.0.1:8000** for the browser demo or **/docs** for Swagger API docs.

### Docker + PostgreSQL + Redis

```bash
docker compose up --build
```

### Online deployment

A production-style `Dockerfile` and `render.yaml` are included for cloud deployment. See [`docs/DEPLOY.md`](docs/DEPLOY.md).

## 🧪 Quality

- GitHub Actions CI
- Automated pytest tests
- Python compilation checks
- Health endpoint
- Typed FastAPI request/response validation
- Environment-variable configuration
- Dockerized runtime

## 🧱 Architecture

**API → AI/RAG/CV services → PostgreSQL/Redis → metrics/evaluation → CI/CD → deployment**

The repository deliberately distinguishes **working local implementations** from integrations that require external model/API credentials. No fake production claims.

## 🛠️ Stack

**Python · FastAPI · PyTorch · OpenCV · YOLO · NumPy · PostgreSQL · Redis · Docker · GitHub Actions · RAG · vector search · agent workflows**

## 📈 Next engineering milestones

- [ ] Connect external LLM provider through secure environment secrets
- [ ] Add real PDF/DOCX ingestion + persistent vector store
- [ ] Add real YOLO video inference + tracking benchmarks
- [ ] Add PostgreSQL persistence and Redis queues to production services
- [ ] Add full integration/evaluation suites
- [ ] Publish public deployed demo and benchmark results

> **Code. Build. Test. Measure. Ship.** 🚀
