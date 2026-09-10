from flask import Flask, render_template, request, redirect, url_for, flash
from database.db import init_db, get_db
from services.workflow import classify_request, process_request

app = Flask(__name__)
app.secret_key = "dev-secret-change-me"

init_db()

@app.route("/")
def index():
    db = get_db()
    requests = db.execute(
        "SELECT * FROM workflow_requests ORDER BY created_at DESC"
    ).fetchall()
    return render_template("index.html", requests=requests)

@app.route("/request", methods=["POST"])
def create_request():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    notes = request.form.get("notes", "").strip()

    if not name or not email or not notes:
        flash("Please complete all fields.", "error")
        return redirect(url_for("index"))

    category, priority, summary = classify_request(notes)
    db = get_db()
    cur = db.execute(
        """INSERT INTO workflow_requests
        (patient_name, email, notes, category, priority, ai_summary, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (name, email, notes, category, priority, summary, "New")
    )
    db.commit()
    process_request(cur.lastrowid)
    flash("Request processed successfully.", "success")
    return redirect(url_for("index"))

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
