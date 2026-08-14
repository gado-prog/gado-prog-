from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Voice AI Assistant", version="0.1.0")

class VoiceRequest(BaseModel):
    text: str = Field(min_length=1, max_length=4000)
    mode: Literal["assistant", "command"] = "assistant"

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/respond")
def respond(request: VoiceRequest) -> dict[str, str]:
    # ASR/TTS providers can be connected through adapters without changing the API.
    return {"mode": request.mode, "text": request.text, "status": "ready-for-provider"}
