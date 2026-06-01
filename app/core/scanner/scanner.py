import shutil
import subprocess
from pathlib import Path
import os

def clone_repository(clone_url: str):

    repo_path = Path("temp_repo")

    # Remove old clone if it exists
    if repo_path.exists():
        shutil.rmtree(repo_path)

    subprocess.run(
        ["git", "clone", clone_url, str(repo_path)],
        check=True
    )

    print(f"Repository cloned successfully: {clone_url}")

    return repo_path

def scan_repository(repo_path):

    print("\nScanning repository...\n")

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            file_path = os.path.join(root, file)

            print(file_path)