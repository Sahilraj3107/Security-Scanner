import os
import shutil
import subprocess
import time
from pathlib import Path
from datetime import datetime

from app.core.scanner.secrets import SECRET_PATTERNS
from app.core.scanner.findings import Finding
from app.core.scanner.semgrep_scanner import run_semgrep_scan


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

    regex_findings = []

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

            # Convert to repository-relative path
            relative_path = os.path.relpath(
                file_path,
                repo_path
            )

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    lines = f.readlines()

                print(f"Scanning: {relative_path}")

                for line_number, line in enumerate(lines, start=1):

                    for secret_name, regex_pattern in SECRET_PATTERNS.items():

                        if regex_pattern.search(line):

                            finding = Finding(
                                type="SECRET",
                                severity="HIGH",
                                file=relative_path,
                                line=line_number,
                                message=f"Hardcoded {secret_name} detected"
                            )

                            regex_findings.append(finding)

                            print("\n[HIGH]")
                            print(f"File: {relative_path}")
                            print(f"Line: {line_number}")
                            print(f"Pattern: {secret_name}")

            except Exception as e:

                print(
                    f"Could not read "
                    f"{relative_path}: {e}"
                )

    print("\nRegex Scan Complete")
    print(f"Regex Findings Found: {len(regex_findings)}")

    print("\nRunning Semgrep Scan...\n")

    semgrep_findings = run_semgrep_scan(repo_path)

    print(
        f"Semgrep Findings Found: "
        f"{len(semgrep_findings)}"
    )

    all_findings = regex_findings + semgrep_findings

    print("\nScan Complete")
    print(f"Total Findings Found: {len(all_findings)}")

    return all_findings


def cleanup_repository(repo_path):

    try:

        # Give Windows a moment to release file handles
        time.sleep(2)

        if os.path.exists(repo_path):

            shutil.rmtree(repo_path)

            print(
                f"\nDeleted temporary repository: "
                f"{repo_path}"
            )

    except Exception as e:

        print(
            f"\nCleanup failed: {e}"
        )