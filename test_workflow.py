from services.workflow import classify_request

def test_appointment():
    category, priority, summary = classify_request(
        "Please reschedule my appointment to next week."
    )
    assert category == "Appointment"
    assert priority == "Medium"
    assert "reschedule" in summary.lower()

def test_billing():
    category, priority, _ = classify_request("I have a question about my invoice.")
    assert category == "Billing"

def test_high_priority():
    category, priority, _ = classify_request("This is urgent and I need help immediately.")
    assert priority == "High"
