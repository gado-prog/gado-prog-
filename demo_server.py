"""Runnable AI portfolio demo.

Run locally: python run_demo.py
API docs: /docs
Browser dashboard: /
"""
from collections import Counter
import re
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Gado AI Portfolio Demo", version="1.1.1")
DOCUMENTS = {
    "ai": "Artificial intelligence systems can combine retrieval, tools, evaluation and structured outputs.",
    "vision": "Computer vision systems can detect objects, track movement and turn video into measurable events.",
    "backend": "FastAPI provides typed HTTP APIs, validation and automatic OpenAPI documentation.",
}
class Ask(BaseModel): question: str = Field(min_length=2, max_length=1000)
class Ticket(BaseModel): message: str = Field(min_length=3, max_length=3000)
class Prediction(BaseModel): features: list[float]
class Research(BaseModel): question: str = Field(min_length=5, max_length=2000)
def tokens(text: str) -> list[str]: return re.findall(r"[a-zA-Zа-яА-Я0-9]+", text.lower())
@app.api_route("/", methods=["GET", "HEAD"], include_in_schema=False)
def home(): return FileResponse(Path(__file__).parent / "static" / "index.html")
@app.get("/health")
def health(): return {"status":"ok","service":"gado-ai-portfolio-demo"}
@app.post("/rag/ask")
def rag_ask(payload: Ask):
    q=Counter(tokens(payload.question)); ranked=[]
    for name,text in DOCUMENTS.items(): ranked.append((sum(q[t] for t in tokens(text) if t in q),name,text))
    score,name,text=max(ranked)
    return {"answer":text,"source":name,"score":score}
@app.post("/agent/research")
def research(payload: Research): return {"question":payload.question,"plan":["decompose","retrieve","check","synthesize"],"status":"completed"}
@app.post("/support/triage")
def triage(payload: Ticket):
    urgent=any(w in payload.message.lower() for w in ("fraud","hacked","security","stolen","payment"))
    return {"route":"human_review" if urgent else "ai_assist","urgent":urgent}
@app.post("/ml/predict")
def predict(payload: Prediction): return {"prediction":sum(payload.features)/len(payload.features) if payload.features else 0.0,"model":"demo-baseline"}
@app.get("/vision/info")
def vision_info(): return {"pipeline":["detect","track","events","metrics"],"status":"ready"}
