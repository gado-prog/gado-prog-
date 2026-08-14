from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Football AI Analyzer", version="0.1.0")

class AnalyzeRequest(BaseModel):
    video_path: str = Field(min_length=1)
    track_players: bool = True
    detect_ball: bool = True

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest) -> dict[str, object]:
    return {"status": "queued", "video": request.video_path, "pipeline": ["detect", "track", "export"]}
