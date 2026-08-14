from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Autonomous Research Agent", version="0.1.0")

class ResearchRequest(BaseModel):
    question: str = Field(min_length=5, max_length=2000)
    depth: Literal["quick", "deep"] = "quick"

class ResearchResponse(BaseModel):
    question: str
    plan: list[str]
    status: Literal["queued", "ready"]

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest) -> ResearchResponse:
    # Provider/tool integrations belong behind this boundary.
    plan = [
        "decompose the question",
        "retrieve relevant evidence",
        "check evidence quality",
        "synthesize a cited report",
    ]
    if request.depth == "deep":
        plan.insert(2, "cross-check conflicting evidence")
    return ResearchResponse(question=request.question, plan=plan, status="ready")
