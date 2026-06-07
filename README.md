# AI-Powered GitHub Security Scanner

An automated GitHub App that performs security analysis on Pull Requests using custom secret detection, Semgrep-based SAST scanning, and AI-generated remediation suggestions.

When a Pull Request is opened or updated, the scanner automatically analyzes the codebase, identifies security issues, generates actionable fix recommendations, and posts the results directly on GitHub as PR comments and status checks.

---

## Features

### GitHub App Integration

* GitHub App authentication using JWT and Installation Tokens
* GitHub Webhook support
* Automatic PR event processing
* GitHub Status Checks integration
* Automated PR comments

### Security Scanning

#### Secret Detection

Custom regex-based detection for:

* API_KEY
* PASSWORD
* SECRET_KEY
* AWS_SECRET

#### Static Application Security Testing (SAST)

Powered by Semgrep:

* Command Injection
* Insecure Deserialization
* Privilege Escalation Risks
* Container Security Issues
* Docker Misconfigurations
* OWASP-style Security Findings

### AI-Powered Remediation Suggestions

For every detected security finding, the scanner generates:

* Security explanation
* Risk assessment
* Suggested remediation steps

Example:

Finding:

Container running as root

AI Suggestion:

Create a dedicated non-root user and switch to it using:

RUN adduser appuser
USER appuser

This follows the principle of least privilege and reduces privilege escalation risks.

### Automated Reporting

Generates a consolidated markdown security report containing:

* Severity
* File location
* Line number
* Security finding
* AI-generated fix suggestion

### GitHub Status Checks

Pull Requests automatically receive status updates:

* Security scan running
* Security findings detected
* No findings detected
* Scan failure

---

## Architecture

Pull Request
↓
GitHub App
↓
GitHub Webhook
↓
FastAPI Backend
↓
Clone Repository
↓
Checkout PR Branch
↓
Regex Security Scan
↓
Semgrep Security Scan
↓
Generate AI Suggestions
↓
Build Security Report
↓
Post GitHub Comment
↓
Update GitHub Status Check

---

## Project Structure

```text
Security-Scanner/
│
├── app/
│   │
│   ├── api/
│   │   └── routes/
│   │       └── webhook.py
│   │
│   ├── core/
│   │   │
│   │   ├── github/
│   │   │   ├── auth.py
│   │   │   ├── comments.py
│   │   │   └── status_checks.py
│   │   │
│   │   └── scanner/
│   │       ├── ai_fixes.py
│   │       ├── findings.py
│   │       ├── report.py
│   │       ├── scanner.py
│   │       ├── secrets.py
│   │       ├── semgrep_scanner.py
│   │       └── __init__.py
│   │
│   ├── config.py
│   └── main.py
│
├── keys/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Technology Stack

### Backend

* FastAPI

### GitHub Integration

* GitHub Apps
* GitHub Webhooks
* GitHub REST API

### Security Tools

* Semgrep
* Custom Regex Scanner

### AI

* Google Gemini API

### Supporting Libraries

* requests
* PyJWT
* cryptography
* pydantic-settings

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Security-Scanner.git

cd Security-Scanner
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GITHUB_APP_ID=your_app_id

GITHUB_PRIVATE_KEY_PATH=keys/github-app-private-key.pem

GITHUB_WEBHOOK_SECRET=your_webhook_secret

GEMINI_API_KEY=your_gemini_api_key
```

---

## Running Locally

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

## Example Security Report

```markdown
# ⚠ Security Scan Report

Total Findings: 2

## HIGH

File: secret_test.py
Line: 1

Hardcoded API_KEY detected

AI Fix Suggestion:

Store secrets in environment variables or a secrets manager instead of hardcoding them in source code.
```

---

## Current Capabilities

* GitHub App Authentication
* GitHub Webhooks
* Repository Cloning
* Branch Checkout
* Secret Detection
* Semgrep SAST Scanning
* AI Fix Suggestions
* GitHub PR Comments
* GitHub Status Checks
* Automated Security Reports

---

## Future Improvements

* Line-Level PR Review Comments
* Security Score Generation
* Scan Only Changed Files
* Background Workers (Redis/Celery)
* Multi-LLM Support
* Security Trend Dashboard

---

