# Optional n8n Integration

A simple n8n workflow can be added later:

1. **Webhook** — receive a JSON request from the Flask application.
2. **IF / Switch** — inspect `category` and `priority`.
3. **Route**:
   - Appointment -> scheduling notification
   - Billing -> billing task
   - Prescription -> clinical-support task
   - High priority -> escalation notification
4. **Database / HTTP Request** — update the request status.
5. **Log** — record the automation result.

Example webhook payload:

```json
{
  "request_id": 101,
  "category": "Appointment",
  "priority": "Medium",
  "assigned_team": "Scheduling Team"
}
```

For a real deployment, add authentication, retries, audit logging,
access controls, and appropriate privacy/security controls.
