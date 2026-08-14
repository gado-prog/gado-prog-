# 🧠 Autonomous Research Agent

A portfolio-grade agentic AI system that decomposes a research question, selects tools, retrieves evidence, synthesizes findings and returns a structured report.

## Architecture

`User → Planner → Search/Tools → Retrieval → Evidence Check → Synthesizer → Report`

## Engineering focus

- Tool calling with strict schemas
- Multi-step planning
- Source-aware answers
- Retry / timeout boundaries
- Structured JSON output
- Evaluation-ready traces

## Suggested stack

Python · FastAPI · Pydantic · RAG · vector search · PostgreSQL/Redis

> Portfolio implementation: external providers and credentials are injected through environment variables.
