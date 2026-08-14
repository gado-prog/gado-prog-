from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Multimodal Knowledge Copilot", version="0.1.0")

class Query(BaseModel):
    question: str = Field(min_length=3, max_length=4000)
    include_images: bool = True

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/query")
def query(payload: Query) -> dict[str, object]:
    return {
        "question": payload.question,
        "retrieval": ["semantic_search", "keyword_search", "reranking"],
        "modalities": ["text", "image"] if payload.include_images else ["text"],
        "answer": "Connect an embedding/vector provider to run retrieval.",
        "sources": [],
    }
