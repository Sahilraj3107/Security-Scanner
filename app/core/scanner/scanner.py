import os
import subprocess
from pathlib import Path
from datetime import datetime

from app.core.scanner.secrets import SECRET_PATTERNS
from app.core.scanner.findings import Finding


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

    findings = []

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

                    lines = f.readlines()

                print(f"Scanning: {file_path}")

                for line_number, line in enumerate(lines, start=1):

                    for secret_name, regex_pattern in SECRET_PATTERNS.items():

                        if regex_pattern.search(line):

                            finding = Finding(
                                type="SECRET",
                                severity="HIGH",
                                file=file_path,
                                line=line_number,
                                message=f"Hardcoded {secret_name} detected"
                            )

                            findings.append(finding)

                            print("\n[HIGH]")
                            print(f"File: {file_path}")
                            print(f"Line: {line_number}")
                            print(f"Pattern: {secret_name}")

            except Exception as e:

                print(f"Could not read {file_path}: {e}")

    print("\nScan Complete")
    print(f"Findings Found: {len(findings)}")

    return findings