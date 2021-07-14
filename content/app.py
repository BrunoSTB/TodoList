from flask import Flask, render_template, session, request, redirect
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps


# Starts Flask
app = Flask(__name__)
app.secret_key = b'\xc8\x95\nj\xd0\x8a\xb6e\xbez\x97\xc6V\x97\xf0\xab'


# Login required decorator
###
# https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
###
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("login")
        return f(*args, **kwargs)
    return decorated_function


##########################
# Note Management

# Index
@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    # Connect to database
    with sqlite3.connect("accounts.db") as database:
        db = database.cursor()

        # Get user's post its
        userNotes = db.execute(
            "SELECT * FROM notes WHERE userid = ?", (session["user_id"], )).fetchall()

        # Create new post it
        if request.method == "POST":
            db.execute("INSERT INTO notes (content, color, userid) VALUES(?,?,?)",
                       (request.form.get("content"), "#2a9d8f", session["user_id"], ))
            database.commit()
            return redirect("/")

        # Render page
        elif request.method == "GET":
            return render_template("index.html", userNotes=userNotes)


# Remove post it
@app.route('/remove', methods=["GET", "POST"])
def remove():
    # Check for correct method & connect to database
    if request.method == "POST":
        with sqlite3.connect("accounts.db") as database:
            db = database.cursor()

            # Get current user post its
            userNotes = db.execute(
                "SELECT * FROM notes WHERE userid = ?", (session["user_id"], )).fetchall()

            # Search for the post it to be deleted in database, then delete it
            for row in userNotes:
                if int(request.form.get('removeBtn')) == int(row[0]):
                    db.execute("DELETE FROM notes WHERE id = ? AND userid = ?", (str(
                        row[0]), session['user_id']))
                    database.commit()
                    return redirect("/")

    return redirect("/")


# Delete All Notes
@app.route('/deleteAll', methods=["POST"])
def delete():
    if request.method == "POST":
        with sqlite3.connect("accounts.db") as database:
            db = database.cursor()

            db.execute("DELETE FROM notes WHERE userid = ?",
                       (session['user_id'], ))
            database.commit()

            return redirect("/")

    return redirect("/")


# Change Postit Color
@app.route('/changeColor', methods=["POST"])
def changeColor():
    with sqlite3.connect("accounts.db") as database:
        db = database.cursor()

        userNotes = db.execute(
            "SELECT * FROM notes WHERE userid = ?", (session["user_id"], )).fetchall()

        # Check which button
        if request.form.get('blueBtn'):
            for row in userNotes:
                if int(request.form.get('blueBtn')) == int(row[0]):
                    db.execute(
                        "UPDATE notes SET color = '#2a9d8f' WHERE id = ? AND userid = ?", (str(row[0]), session["user_id"]))

        elif request.form.get('yellowBtn'):
            for row in userNotes:
                if int(request.form.get('yellowBtn')) == int(row[0]):
                    db.execute(
                        "UPDATE notes SET color = '#e9c46a' WHERE id = ? AND userid = ?", (str(row[0]), session["user_id"]))

        elif request.form.get('orangeBtn'):
            for row in userNotes:
                if int(request.form.get('orangeBtn')) == int(row[0]):
                    db.execute(
                        "UPDATE notes SET color = '#f4a261' WHERE id = ? AND userid = ?", (str(row[0]), session["user_id"]))

        elif request.form.get('redBtn'):
            for row in userNotes:
                if int(request.form.get('redBtn')) == int(row[0]):
                    db.execute(
                        "UPDATE notes SET color = '#e76f51' WHERE id = ? AND userid = ?", (str(row[0]), session["user_id"]))

        database.commit()
        return redirect("/")


##########################
# User management

# User Login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # FORGET USER ID
        session.clear()

        with sqlite3.connect("accounts.db") as database:
            db = database.cursor()

            # CHECK IF BOTH USERNAME AND PASSWORD WERE INPUTED
            if not request.form.get('username') or not request.form.get('password'):
                return render_template("login.html")

            # CHECK IF USERNAME EXISTS
            if db.execute("SELECT username FROM users WHERE username = ?", (request.form.get('username'), )) == False:
                return render_template("login.html")

            # CHECK IF PASSWORD MATCHES
            hashed_pass = db.execute("SELECT hashed_pass FROM users WHERE username = ?", (request.form.get('username'), )).fetchall()
            if not hashed_pass:
                return render_template("login.html")

            if check_password_hash(hashed_pass[0][0], request.form.get('password')):
                session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", (request.form.get('username'), )).fetchall()[0][0]
                return redirect("/")

    return render_template("login.html")



# Log out
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/login")


# Register
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        with sqlite3.connect("accounts.db") as database:
            db = database.cursor()

            # CHECK IF USERNAME AND PASSWORD WERE INPUTED
            if not request.form.get('username') or not request.form.get('password'):
                return render_template("register.html")

            # CHECK IF USERNAME IS AVAILABLE
            rows = db.execute("SELECT username FROM users WHERE username = ?",
                              (request.form.get('username'), )).fetchall()

            if len(rows) != 0:
                return render_template("register.html")

            # CHECK IF PASSWORDS MATCH
            elif request.form.get("password") == request.form.get("passwordRepeat"):

                # CREATE ACCOUNTS
                db.execute("INSERT INTO users (username, hashed_pass) VALUES (?, ?)",
                           (request.form.get('username'),
                            generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)))

                database.commit()
                return render_template("login.html")

    return render_template("register.html")
