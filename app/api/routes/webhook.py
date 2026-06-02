from fastapi import APIRouter, Request
from app.core.scanner.report import generate_report

from app.core.scanner.scanner import (
    clone_repository,
    scan_repository
)

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

    # Clone repository only for relevant PR actions
    if action in ["opened", "synchronize", "reopened"]:

        print("\nStarting repository clone...")

        repo_path = clone_repository(
                        clone_url,
                        head_ref
                    )

        print(f"Local Path: {repo_path}")

        findings = scan_repository(repo_path)
        report = generate_report(findings)
        print("\nScan Report:\n") 
        print(report)

    print("=" * 50 + "\n")

    return {"status": "received"}