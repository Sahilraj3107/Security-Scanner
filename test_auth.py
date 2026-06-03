from app.core.github.auth import get_installation_token

token = get_installation_token()

print(token[:20])