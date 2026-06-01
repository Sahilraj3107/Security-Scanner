from fastapi import FastAPI

app = FastAPI(
    title="Security Scanner",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Security Scanner Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }