import shutil
import subprocess
from pathlib import Path
import os
from datetime import datetime


def clone_repository(clone_url: str):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    repo_path = Path(f"temp_repo_{timestamp}")

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