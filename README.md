# Healthcare Workflow Automation System

A portfolio project demonstrating **Python scripting, SQL, AI-assisted text processing, REST/web development, and business workflow automation**.

> This is an educational portfolio demo. Use synthetic data only. Do not enter real patient health information.

## Problem

Healthcare and US-business-process teams often receive repetitive requests such as appointment changes, billing questions, prescription requests, and general inquiries. Manually reading, categorizing, prioritizing, and routing every request can be time-consuming.

## Solution

This application:
1. Accepts a request through a web form.
2. Validates the input.
3. Classifies the request into a business category.
4. Assigns a priority.
5. Creates a short AI-style summary.
6. Routes the request to the appropriate team.
7. Escalates high-priority requests.
8. Records an automation log.

The classification layer is intentionally deterministic in the starter version so the project works without an API key. An external LLM can be added later behind `services/ai_service.py`.

## Tech Stack

- Python
- Flask
- SQLite / SQL
- HTML/CSS
- REST-style health endpoint
- pytest
- Git/GitHub
- Optional n8n/Power Automate webhook integration

## Run locally

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

### Run tests

```powershell
pytest
```

## Example workflow

Input:
> I need to reschedule my appointment to next week.

Result:
- Category: Appointment
- Priority: Medium
- Team: Scheduling Team
- Status: Routed

Input:
> This is urgent and I need help immediately.

Result:
- Priority: High
- Status: Escalated

## SQL practice

Example query:

```sql
SELECT category, COUNT(*) AS request_count
FROM workflow_requests
GROUP BY category
ORDER BY request_count DESC;
```

## Automation extension

A production-style version can connect the `process_request()` event to n8n or Power Automate. The external workflow can:
- receive a webhook,
- create a task,
- send a notification,
- update the status,
- write an audit record.

## Portfolio talking points

"I built a Python-based healthcare workflow automation demo to show how repetitive business requests can be classified, prioritized, routed, and logged. I used Flask for the web layer, SQLite for persistence, Python for the workflow engine, and pytest for testing. I kept the initial AI layer deterministic so the application could run locally without exposing sensitive data or requiring an API key."

## Important

This project is a portfolio simulation, not a clinical system. Do not use real patient data.
