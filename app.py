import sqlite3
import config
import datetime as dt
from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import db

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT id, password_hash FROM Users WHERE username = ?"
    user_id, password_hash = db.query(sql, [username])[0]

    if check_password_hash(password_hash, password):
        session["username"] = username
        session["user_id"] = user_id
        return redirect("/")
    else:
        return "VIRHE: Väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/create/user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: Salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO Users (username, password_hash) VALUES (?,?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: Tunnus on jo valittu"

    return "Tunnus luotu"

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/create/event", methods=["GET", "POST"])
def create():
    if request.method=="GET":
        sql_users = "SELECT id, username FROM Users"
        sql_tags = "SELECT id, tag FROM Tags"
        users = db.query(sql_users)
        my_id_at = [u[0] for u in users].index(session["user_id"])
        users.pop(my_id_at)
        tags = db.query(sql_tags)
        print(users)
        return render_template("create_event.html", users=users, tags=tags)
    
    movie = request.form["movie"]
    location = request.form["location"]
    showtime = request.form["showtime"]
    users = [session["user_id"]]
    users += request.form.getlist("users")
    list(set(users))
    tags = request.form.getlist("tags")
    new_tag = request.form["new-tag"]
    db.add_event(movie, location, showtime, users, tags, new_tag)

    return redirect("/")