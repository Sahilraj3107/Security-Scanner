import time
import jwt
import requests

from app.config import settings


def generate_jwt():

    with open(
        settings.github_private_key_path,
        "r"
    ) as f:

        private_key = f.read()

    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + 600,
        "iss": settings.github_app_id
    }

    encoded_jwt = jwt.encode(
        payload,
        private_key,
        algorithm="RS256"
    )

    return encoded_jwt


def get_installation_token():

    jwt_token = generate_jwt()

    url = (
        "https://api.github.com/app/"
        f"installations/"
        f"{settings.github_installation_id}"
        "/access_tokens"
    )

    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.post(
        url,
        headers=headers
    )

    response.raise_for_status()

    return response.json()["token"]