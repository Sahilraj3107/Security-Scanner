import re

SECRET_PATTERNS = {
    "API_KEY": re.compile(
        r'API_KEY\s*=\s*["\'][^"\']+["\']'
    ),

    "PASSWORD": re.compile(
        r'PASSWORD\s*=\s*["\'][^"\']+["\']'
    ),

    "SECRET_KEY": re.compile(
        r'SECRET_KEY\s*=\s*["\'][^"\']+["\']'
    ),

    "AWS_SECRET": re.compile(
        r'AWS_SECRET\s*=\s*["\'][^"\']+["\']'
    )
}