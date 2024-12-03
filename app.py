# Description: This file contains the main code for the Flask app.


# import
from flask import Flask, render_template, request, flash, redirect, session
from flask_session import Session
from models import db, User, Message
from werkzeug.security import generate_password_hash
import os


# create app
app = Flask(__name__)

# reload templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

# configure database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chatterbox.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# home page
@app.route("/")
def home():
    return render_template("home.html")


# author page
@app.route("/author")
def author():
    return render_template("author.html")


# login page
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


# register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # check if username and password are provided
        if not username or not password:
            flash("Username and password are required!")
            return redirect("/register")
        
        # check if username already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists!")
            return redirect("/register")
        
        # check password length
        if len(password) < 8:
            flash("Password must be at least 8 characters long!")
            return redirect("/register")
        
        # create a new user
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please log in.")
        return redirect("/login")
    
    return render_template("register.html")


# run the app
if __name__ == "__main__":
    app.run(debug=True)