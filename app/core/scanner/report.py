def generate_report(findings):

    report = "# ⚠ Security Scan Report\n\n"

    report += (
        f"**Total Findings:** "
        f"{len(findings)}\n\n"
    )

    if not findings:

        report += (
            "✅ No security findings found."
        )

        return report

    for finding in findings:

        report += (
            f"## {finding.severity}\n\n"
            f"- File: `{finding.file}`\n"
            f"- Line: `{finding.line}`\n"
            f"- Message: {finding.message}\n\n"
        )

    return report