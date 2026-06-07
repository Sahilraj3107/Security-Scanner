import json
import os
import subprocess

from app.core.scanner.findings import Finding


def map_severity(severity: str) -> str:
    mapping = {
        "INFO": "LOW",
        "WARNING": "MEDIUM",
        "ERROR": "HIGH"
    }

    return mapping.get(severity, "MEDIUM")


def run_semgrep_scan(repo_path: str):
    findings = []

    try:
        result = subprocess.run(
            [
                "semgrep",
                "--config",
                "auto",
                "--json",
                repo_path
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        data = json.loads(result.stdout)

        for issue in data.get("results", []):

            findings.append(
                Finding(
                    type="Semgrep",
                    severity=map_severity(
                        issue.get("extra", {}).get("severity", "WARNING")
                    ),
                    file=os.path.relpath(
                        issue.get("path", ""),
                        repo_path
                    ),
                    line=issue.get("start", {}).get("line", 0),
                    message=issue.get("extra", {}).get("message", "")
                )
            )

    except Exception as e:
        print(f"Semgrep scan failed: {e}")

    return findings