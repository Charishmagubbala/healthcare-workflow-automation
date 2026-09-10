import re
from database.db import get_db

URGENT_WORDS = {
    "urgent", "emergency", "severe", "critical", "immediately",
    "chest pain", "difficulty breathing"
}

def classify_request(notes):
    text = notes.lower()

    if any(word in text for word in URGENT_WORDS):
        priority = "High"
    elif any(word in text for word in ("appointment", "schedule", "reschedule", "visit")):
        priority = "Medium"
    else:
        priority = "Low"

    if any(word in text for word in ("billing", "invoice", "payment", "insurance")):
        category = "Billing"
    elif any(word in text for word in ("appointment", "schedule", "reschedule", "visit")):
        category = "Appointment"
    elif any(word in text for word in ("prescription", "medicine", "medication", "refill")):
        category = "Prescription"
    else:
        category = "General Inquiry"

    summary = re.sub(r"\s+", " ", notes).strip()
    if len(summary) > 180:
        summary = summary[:177] + "..."

    return category, priority, summary

def process_request(request_id):
    db = get_db()
    row = db.execute(
        "SELECT category, priority FROM workflow_requests WHERE id = ?",
        (request_id,)
    ).fetchone()

    team_map = {
        "Billing": "Billing Operations",
        "Appointment": "Scheduling Team",
        "Prescription": "Clinical Support",
        "General Inquiry": "Customer Support"
    }
    team = team_map.get(row["category"], "Customer Support")

    status = "Escalated" if row["priority"] == "High" else "Routed"
    db.execute(
        "UPDATE workflow_requests SET assigned_team = ?, status = ? WHERE id = ?",
        (team, status, request_id)
    )
    db.execute(
        "INSERT INTO automation_logs (request_id, action, details) VALUES (?, ?, ?)",
        (request_id, "Automatic routing",
         f"Assigned to {team}; priority={row['priority']}")
    )
    db.commit()
    db.close()
