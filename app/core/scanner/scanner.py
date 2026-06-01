import os
import subprocess
from pathlib import Path
from datetime import datetime

from app.core.scanner.secrets import SECRET_PATTERNS


def clone_repository(clone_url: str, branch_name: str):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    repo_path = Path(f"temp_repo_{timestamp}")

    # Clone repository
    subprocess.run(
        ["git", "clone", clone_url, str(repo_path)],
        check=True
    )

    # Checkout PR branch
    subprocess.run(
        ["git", "checkout", branch_name],
        cwd=repo_path,
        check=True
    )

    print(f"Repository cloned successfully: {clone_url}")
    print(f"Checked out branch: {branch_name}")

    return repo_path


def scan_repository(repo_path):

    print("\nScanning repository...\n")

    skip_dirs = {
        ".git",
        "__pycache__",
        ".pytest_cache",
        "venv"
    }

    for root, dirs, files in os.walk(repo_path):

        # Skip unwanted directories
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for file in files:

            file_path = os.path.join(root, file)

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read()

                    print(f"Scanning: {file_path}")

                    for pattern in SECRET_PATTERNS:

                        if pattern in content:

                            print("\n[HIGH]")
                            print(f"File: {file_path}")
                            print(f"Pattern: {pattern}")

            except Exception as e:

                print(f"Could not read {file_path}: {e}")