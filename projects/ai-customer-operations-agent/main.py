from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI Customer Operations Agent", version="0.1.0")

class Ticket(BaseModel):
    message: str = Field(min_length=3, max_length=5000)
    priority: Literal["normal", "urgent"] = "normal"

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/triage")
def triage(ticket: Ticket) -> dict[str, object]:
    urgent = ticket.priority == "urgent" or any(w in ticket.message.lower() for w in ["fraud", "security", "account hacked"])
    return {
        "route": "human_review" if urgent else "ai_assist",
        "priority": "urgent" if urgent else ticket.priority,
        "requires_approval": urgent,
    }
