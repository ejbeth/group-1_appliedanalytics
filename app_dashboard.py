from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return '<p>Go to <a href="/dashboard">/dashboard</a></p>'

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard", active="dashboard")

@app.route("/team")
def team():
    return render_template("team.html", title="Team", active="team")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects", active="projects")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html", title="Calendar", active="calendar")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title="Contacts", active="contacts")
