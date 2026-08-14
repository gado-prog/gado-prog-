from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ML API Starter", version="0.1.0")

class PredictionRequest(BaseModel):
    features: list[float]

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/predict")
def predict(request: PredictionRequest) -> dict[str, object]:
    # Replace this deterministic placeholder with a loaded model.
    score = sum(request.features) / max(len(request.features), 1)
    return {"prediction": score, "model_version": "demo-0.1.0"}
