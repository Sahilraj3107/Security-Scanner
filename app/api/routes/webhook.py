# from fastapi import APIRouter, Request

# router = APIRouter()


# @router.post("/webhook/github")
# async def github_webhook(request: Request):

#     payload = await request.json()

#     action = payload.get("action")

#     pr = payload.get("pull_request", {})

#     repo = payload.get("repository", {})

#     print("\n" + "=" * 50)
#     print("GitHub PR Event Received")
#     print("=" * 50)

#     print("Action:", action)
#     print("PR Number:", pr.get("number"))
#     print("PR Title:", pr.get("title"))
#     print("Repository:", repo.get("full_name"))

#     return {"status": "received"}

#This is just a test script
from fastapi import APIRouter, Request
import json

router = APIRouter()

@router.post("/webhook/github")
async def github_webhook(request: Request):

    payload = await request.json()

    print("\n" + "=" * 50)
    print(json.dumps(payload, indent=2))
    print("=" * 50)

    return {"status": "received"}