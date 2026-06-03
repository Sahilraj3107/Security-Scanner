import requests

from app.core.github.auth import get_installation_token


def post_pr_comment(
    repo_name: str,
    pr_number: int,
    report: str
):

    token = get_installation_token()

    url = (
        f"https://api.github.com/repos/"
        f"{repo_name}/issues/{pr_number}/comments"
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "body": report
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print(
        f"GitHub Comment Response: "
        f"{response.status_code}"
    )

    if response.status_code == 201:

        print(
            f"Comment posted to PR #{pr_number}"
        )

    else:

        print(response.text)