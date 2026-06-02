def generate_report(findings):

    report = []

    report.append("Security Scan Report")
    report.append("=" * 30)
    report.append(f"Total Findings: {len(findings)}")
    report.append("")

    for finding in findings:

        report.append(f"[{finding.severity}]")
        report.append(f"File: {finding.file}")
        report.append(f"Line: {finding.line}")
        report.append(f"Message: {finding.message}")
        report.append("")

    return "\n".join(report)