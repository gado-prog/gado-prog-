from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI Document Assistant", version="0.1.0")

class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=4000)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/ask")
def ask(request: AskRequest) -> dict[str, object]:
    return {"question": request.question, "answer": "Connect a document retriever/LLM provider.", "sources": []}
