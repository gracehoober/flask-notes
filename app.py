import os

from flask import Flask, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User, Note
from forms import RegisterForm, LoginForm, CSRFProtectForm, NoteForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///notes_app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
debug = DebugToolbarExtension(app)


#REGISTRATION ROUTES

@app.get("/")
def homepage():
    """Homepage: redirect to /register"""

    return redirect("/register")

@app.route("/register", methods = ["GET", "POST"])
def register_user():
    """Register a user: produce form and handle form submission"""

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        # if User.query.filter(User.username==username).one_or_none:
        #     flash("Username already exists!")
        #     return render_template('register.html',form=form)

        # if User.query.filter(User.email==email).one_or_none:
        #     flash("Email already exists!")
        #     return render_template('register.html',form=form)

        user = User.register(username, password, email, first_name, last_name)

        db.session.add(user)
        db.session.commit()
        session["user_id"] = username

        return redirect(f'/users/{username}')
    else:
        return render_template('register.html',form=form)

# LOGIN ROUTES

@app.route('/login', methods=["GET","POST"])
def user_login():
    """Renders user login page and handles username/pw validation"""

    if "user_id" in session:
        return redirect(f'/users/{session["user_id"]}')

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        auth_user = User.authenticate(username,password)

        if auth_user:
            session["user_id"] = auth_user.username
            return redirect(f'/users/{username}')

        else:
            form.username.errors = ["Invalid Credentials"]

    return render_template('login.html',form=form)


@app.get("/users/<username>")
def user_page(username):
    """Renders user page"""

    user = User.query.get_or_404(username)

    form = CSRFProtectForm()

    if "user_id" not in session:
        return redirect('/login')

    if session["user_id"] == user.username:

        return render_template('user_page.html',user=user,form=form)
    else:
        flash("You must be logged in to view!")
        return redirect("/login")


@app.post("/logout")
def logout_user():
    """Logs user out and redirects to homepage."""

    form = CSRFProtectForm()

    if form.validate_on_submit():
        # Remove "user_id" if present, but no errors if it wasn't
        session.pop("user_id", None)

    return redirect("/")

#User routes

@app.post("/users/<username>/delete")
def delete_user(username):
    """Remove user from database"""
    user = User.query.get_or_404(username)
    notes = user.notes

    for note in notes:
        db.session.delete(note)
    # db.session.commit()

    db.session.delete(user)
    db.session.commit()

    return redirect("/")

@app.route("/users/<username>/notes/add", methods=["GET", "POST"])
def add_note(username):
    """Create a note: produce note form and note submission."""

    # if "user_id" in session:
    #     return redirect(f'/users/{session["user_id"]}')

    form = NoteForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_note= Note(title=title, content=content, owner_username=username)

        db.session.add(new_note)
        db.session.commit()

        return redirect(f'/users/{username}')

    else:
        return render_template("note_add.html", form=form)
