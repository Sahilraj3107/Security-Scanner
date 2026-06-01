from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class WebhookPayload(BaseModel):
    event: str
    pr: int


@router.post("/webhook/github")
async def github_webhook(payload: WebhookPayload):

    print("=" * 50)
    print("GitHub Event Received")
    print(payload.model_dump())
    print("=" * 50)

    return {"status": "received"}