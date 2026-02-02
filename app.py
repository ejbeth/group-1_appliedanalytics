from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return '<p>Go to <a href="/login">/login</a></p>'

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if username == "renato" and password == "123":
        return render_template("success.html", username=username)

    return render_template("login.html", error="Invalid credentials")
if __name__ == "__main__":
    app.run(debug=True)