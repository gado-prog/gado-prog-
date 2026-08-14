from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Football Intelligence Platform", version="0.1.0")

class VideoJob(BaseModel):
    source: str = Field(min_length=1)
    detect_ball: bool = True
    track_players: bool = True

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/jobs")
def create_job(job: VideoJob) -> dict[str, object]:
    return {
        "status": "queued",
        "source": job.source,
        "pipeline": ["detection", "tracking", "event extraction", "metrics"],
        "options": {"detect_ball": job.detect_ball, "track_players": job.track_players},
    }
