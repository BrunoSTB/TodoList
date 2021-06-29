from flask import Flask, render_template, session, request, redirect
from flask_session import Session
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash


# Starts Flask
app = Flask(__name__)
app.secret_key = b'\xc8\x95\nj\xd0\x8a\xb6e\xbez\x97\xc6V\x97\xf0\xab'


@app.route('/')
def index():
    return render_template("index.html")

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
            if not db.execute( "SELECT username FROM users WHERE username = ?", (request.form.get('username'), ) ):
                return render_template("login.html")

            # CHECK IF PASSWORD MATCHES
            hashed_pass =  db.execute( "SELECT hashed_pass FROM users WHERE username = ?", (request.form.get('username'), ) ).fetchall()
            if check_password_hash( hashed_pass[0][0], request.form.get('password') ):
                session["user_id"] = db.execute( "SELECT id FROM users WHERE username = ?", (request.form.get('username'), ) ).fetchall()[0][0]
                return redirect("/")
            
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        with sqlite3.connect("accounts.db") as database:
            db = database.cursor()

            # CHECK IF USERNAME AND PASSWORD WERE INPUTED
            if not request.form.get('username') or not request.form.get('password'):
                print("1")
                return render_template("register.html")

            # CHECK IF USERNAME IS AVAILABLE
            rows = db.execute("SELECT username FROM users WHERE username = ?", (request.form.get('username'), ) ).fetchall()
            if len(rows) != 0: 
                
                return render_template("register.html")

            # CHECK IF PASSWORDS MATCH
            elif request.form.get("password") == request.form.get("passwordRepeat"):
                # CREATE ACCOUNTS
                db.execute("INSERT INTO users (username, hashed_pass) VALUES (?, ?)", 
                           (request.form.get('username'), 
                           generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)) )
                database.commit()
                return render_template("login.html")    

    return render_template("register.html")