from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()


# 1. Define the metric (A counter to track page views)
REQUEST_COUNTER = Counter("my_app_requests_total", "Total number of visits to the app")

@app.get("/")
def home():
    # 2. Increment the metric when the route is hit
    REQUEST_COUNTER.inc()
    return {"message": "Hello, Prometheus! By Gowtham!!!"}

@app.get("/metrics")
def metrics():
    # 3. Expose the metrics in the text format Prometheus expects
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

