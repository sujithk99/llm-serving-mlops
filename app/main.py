from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import Response
import time

app = FastAPI()

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total API Requests"
)

REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds",
    "API Request Latency"
)

generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

class Request(BaseModel):
    prompt: str

@app.get("/ping")
def ping():
    REQUEST_COUNT.inc()
    return {"status": "healthy"}

@app.post("/invocations")
def invoke(req: Request):

    REQUEST_COUNT.inc()

    start = time.time()

    result = generator(
        req.prompt,
        max_new_tokens=50
    )

    REQUEST_LATENCY.observe(time.time() - start)

    return {
        "response": result[0]["generated_text"]
    }

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )