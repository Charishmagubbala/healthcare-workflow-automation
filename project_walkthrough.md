# Project Walkthrough

## 1. User submits a request
The form in `templates/index.html` sends the name, email, and request text to `/request`.

## 2. Python validates the input
`app.py` checks that required fields are present.

## 3. Classification
`services/workflow.py` determines:
- category
- priority
- short summary

## 4. SQL persistence
SQLite stores the request in `workflow_requests`.

## 5. Automation
`process_request()` selects the correct business team and status.

## 6. Audit trail
Every automatic routing action is stored in `automation_logs`.

## 7. Dashboard
The home page displays the processed workflow requests.

## Suggested future improvements
- Login/authentication
- PostgreSQL
- Docker
- REST API documentation
- Real LLM integration using environment variables
- n8n/Power Automate integration
- Email/Teams notifications
- Role-based access control
- More comprehensive tests
