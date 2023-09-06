from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import Email, InputRequired, Length


class RegisterForm(FlaskForm):
    """Form for registering user"""

    username = StringField(
        "User Name", validators=[
            InputRequired(), Length(min=4, max=20,
            message= "user name must be between 4-20 characters")
        ])

    password = PasswordField(
        "Password",
        validators=[
            InputRequired(), Length(min=4, max=100,
            message= "password must be between 4-20 characters")
        ])

    email = StringField(
        "Email Address",
        validators=[
            InputRequired(),
            Email(),
            Length(min=4, max=50)])

    first_name = StringField(
        "First Name",
        validators=[
            InputRequired(),
            Length(min=4, max=30,
            message= "first name must be between 4-20 characters")
        ])

    last_name = StringField(
        "Last Name",
        validators=[
            InputRequired(),
            Length(min=4, max=30,
                   message= "last name must be between 4-20 characters")
        ])



class LoginForm(FlaskForm):
    """Form for logging in User"""

    username = StringField("User Name",
                           validators=[InputRequired()])

    password = PasswordField("Password",
                           validators=[InputRequired()])

class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""

class NoteForm(FlaskForm):
    """Form for new note"""

    title= StringField("Note title",
                       validators=[
                           InputRequired(),
                           Length(min=0,
                                  max=100,
                                  message="title exceeds character limit")])
    
    content= TextAreaField("Note text",
                           validators=[
                           InputRequired(),
                           Length(min=0,
                                  max=10000,
                                  message="note exceeds character limit")])