from flask import Flask, render_template, request

app = Flask(__name__)

# Demo data (temporary) so pages can work even without a database
ORDERS = [
    {"id": 1001, "status": "Submitted", "total": 120.50},
    {"id": 1002, "status": "Approved", "total": 89.99},
    {"id": 1003, "status": "Rejected", "total": 45.00},
]

@app.route("/")
def home():
    return """
    <p><a href="/login">Login</a></p>
    <p><a href="/orders">Orders</a></p>
    <p><a href="/report">Report</a></p>
    <p><a href="/terms">Terms & Conditions</a></p>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if username == "renato" and password == "123":
        return render_template("success.html", username=username)

    return render_template("login.html", error="Invalid credentials")

@app.route("/orders")
def orders():
    return render_template("pages/order_view.html", orders=ORDERS)

@app.route("/report")
def report():
    metrics = {
        "total_orders": len(ORDERS),
        "submitted": sum(1 for o in ORDERS if o["status"] == "Submitted"),
        "approved": sum(1 for o in ORDERS if o["status"] == "Approved"),
        "rejected": sum(1 for o in ORDERS if o["status"] == "Rejected"),
    }
    return render_template("pages/report.html", metrics=metrics)

@app.route("/terms")
def terms():
    return render_template("pages/Terms_Cond.html")

if __name__ == "__main__":
    app.run(debug=True)