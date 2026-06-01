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

#Just a test script
from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/webhook/github")
async def github_webhook(request: Request):

    payload = await request.json()

    action = payload.get("action")

    pr = payload.get("pull_request", {})
    repo = payload.get("repository", {})

    repo_name = repo.get("full_name")
    clone_url = repo.get("clone_url")

    pr_number = payload.get("number")

    head = pr.get("head", {})
    head_sha = head.get("sha")
    head_ref = head.get("ref")

    print("\n" + "=" * 50)
    print("GitHub PR Event Received")
    print("=" * 50)

    print(f"Action: {action}")
    print(f"Repository: {repo_name}")
    print(f"Clone URL: {clone_url}")
    print(f"PR Number: {pr_number}")
    print(f"Branch: {head_ref}")
    print(f"Head SHA: {head_sha}")

    print("=" * 50 + "\n")

    return {"status": "received"}