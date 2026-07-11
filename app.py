from flask import Flask, render_template, request

app = Flask(__name__)

# Your personal info (customize this)
my_info = {
    "name": "Jahnavi S T",
    "title": "Data Science & Engineering Student",
    "about": "Final year student passionate about AI, distributed systems, and building practical projects.",
    "skills": ["Python", "Java", "Flask", "React", "Pandas", "LangChain", "PostgreSQL"],
    "projects": [
        {"name": "GHOST Protocol", "desc": "Behavioral trust monitor for AI agents using Isolation Forest."},
        {"name": "SentinelLog", "desc": "Distributed logging system with TCP collector, Flask API, and React dashboard."},
        {"name": "CompanyBrain", "desc": "RAG-based AI knowledge OS for internal company documents."}
    ]
}


@app.route("/")
def index():
    return render_template("index.html", info=my_info)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    message_sent = False
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now, just print to console (later could save to file/db/email)
        print(f"New message from {name} ({email}): {message}")
        message_sent = True

    return render_template("contact.html", message_sent=message_sent)


if __name__ == "__main__":
    app.run(debug=True)