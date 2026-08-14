"""One-command local demo for the portfolio.

Run: uvicorn demo_server:app --reload
Docs: http://127.0.0.1:8000/docs
"""
from collections import Counter
import re
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Gado AI Portfolio Demo", version="1.0.0")

DOCUMENTS = {
    "ai": "Artificial intelligence systems can combine retrieval, tools, evaluation and structured outputs.",
    "vision": "Computer vision systems can detect objects, track movement and turn video into measurable events.",
    "backend": "FastAPI provides typed HTTP APIs, validation and automatic OpenAPI documentation.",
}

class Ask(BaseModel):
    question: str = Field(min_length=2, max_length=1000)

class Ticket(BaseModel):
    message: str = Field(min_length=3, max_length=3000)

class Prediction(BaseModel):
    features: list[float]

class Research(BaseModel):
    question: str = Field(min_length=5, max_length=2000)


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-zA-Zа-яА-Я0-9]+", text.lower())

@app.get("/health")
def health():
    return {"status": "ok", "service": "gado-ai-portfolio-demo"}

@app.post("/rag/ask")
def rag_ask(payload: Ask):
    q = Counter(tokens(payload.question))
    ranked = []
    for name, text in DOCUMENTS.items():
        score = sum(q[t] for t in tokens(text) if t in q)
        ranked.append((score, name, text))
    ranked.sort(reverse=True)
    score, name, text = ranked[0]
    return {"answer": text, "source": name, "score": score}

@app.post("/agent/research")
def research(payload: Research):
    steps = ["decompose", "retrieve", "check", "synthesize"]
    return {"question": payload.question, "plan": steps, "status": "completed"}

@app.post("/support/triage")
def triage(payload: Ticket):
    text = payload.message.lower()
    urgent_words = ("fraud", "hacked", "security", "stolen", "payment")
    urgent = any(word in text for word in urgent_words)
    return {"route": "human_review" if urgent else "ai_assist", "urgent": urgent}

@app.post("/ml/predict")
def predict(payload: Prediction):
    if not payload.features:
        return {"prediction": 0.0}
    return {"prediction": sum(payload.features) / len(payload.features), "model": "demo-baseline"}

@app.get("/vision/info")
def vision_info():
    return {"pipeline": ["detect", "track", "events", "metrics"], "status": "ready"}
