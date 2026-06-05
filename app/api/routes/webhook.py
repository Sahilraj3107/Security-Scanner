from fastapi import APIRouter, Request

from app.core.scanner.report import generate_report
from app.core.github.comments import post_pr_comment
from app.core.scanner.scanner import (
    clone_repository,
    scan_repository
)
from app.core.github.status_checks import (
    create_status_check
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

    # Process only relevant PR events
    if action in ["opened", "synchronize", "reopened"]:

        try:

            # Set status to pending
            create_status_check(
                repo_name=repo_name,
                commit_sha=head_sha,
                state="pending",
                description="Security scan running..."
            )

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

            print("\nPosting comment to GitHub...\n")

            post_pr_comment(
                repo_name=repo_name,
                pr_number=pr_number,
                report=report
            )

            # Update status based on findings
            if findings:

                create_status_check(
                    repo_name=repo_name,
                    commit_sha=head_sha,
                    state="failure",
                    description=f"{len(findings)} finding(s) detected"
                )

            else:

                create_status_check(
                    repo_name=repo_name,
                    commit_sha=head_sha,
                    state="success",
                    description="No security findings"
                )

        except Exception as e:

            print(f"\nScanner Error: {e}")

            create_status_check(
                repo_name=repo_name,
                commit_sha=head_sha,
                state="failure",
                description="Scanner crashed"
            )

            raise

    print("=" * 50 + "\n")

    return {"status": "received"}