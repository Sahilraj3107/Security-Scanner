import requests

from app.core.github.auth import get_installation_token


def create_status_check(
    repo_name: str,
    commit_sha: str,
    state: str,
    description: str
):
    """
    state:
        success
        failure
        pending
    """

    token = get_installation_token()

    url = (
        f"https://api.github.com/repos/"
        f"{repo_name}/statuses/{commit_sha}"
    )

    payload = {
        "state": state,
        "description": description,
        "context": "Security Scanner"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print(
        f"Status Check Response: "
        f"{response.status_code}"
    )

    return response