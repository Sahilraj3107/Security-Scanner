from fastapi import FastAPI

from app.api.routes.webhook import router as webhook_router

app = FastAPI(
    title="Security Scanner",
    version="1.0.0"
)

app.include_router(webhook_router)


@app.get("/")
async def root():
    return {"message": "Security Scanner Running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}