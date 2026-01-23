from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "skybooker_secret"

def get_db():
    return sqlite3.connect("airline.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        db = get_db()
        db.execute(
            "INSERT INTO users(username, password) VALUES (?,?)",
            (request.form["username"], request.form["password"])
        )
        db.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (request.form["username"], request.form["password"])
        ).fetchone()
        if user:
            session["user"] = user[1]
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/flights")
def flights():
    db = get_db()
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/book/<int:flight_id>")
def book(flight_id):
    db = get_db()
    flight = db.execute("SELECT * FROM flights WHERE id=?", (flight_id,)).fetchone()
    db.execute(
        "INSERT INTO bookings(flight_id, booking_time) VALUES (?,?)",
        (flight_id, datetime.now())
    )
    db.commit()
    return render_template("eticket.html", flight=flight)

if __name__ == "__main__":
    app.run(debug=True)
