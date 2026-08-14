from time import perf_counter
from fastapi import FastAPI, Request

app = FastAPI(title="ML Observability Platform", version="0.1.0")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.middleware("http")
async def request_metrics(request: Request, call_next):
    started = perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time-Ms"] = f"{(perf_counter() - started) * 1000:.2f}"
    return response

@app.get("/metrics/demo")
def metrics_demo() -> dict[str, object]:
    return {
        "requests_total": 0,
        "errors_total": 0,
        "p95_latency_ms": None,
        "evaluation_status": "not_run",
    }
