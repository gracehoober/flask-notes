import os

from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User
#from forms import

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///notes_app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.get("/")
def homepage():
    """Homepage: redirect to /register"""

    return redirect("/register")

@app.route("/register", methods = ["GET", "POST"])
def register_user():
    """Register a user: produce form and handle form submission"""

# make a form and then instantiate it
    form = RegisterForm()
# validate the form
    # grab from form
    # add info to db
    # save user in the current session
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password)

# fails validation
    # render the template, form



