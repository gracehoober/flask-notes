from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, InputRequired


class RegisterForm(FlaskForm):
    """Form for registering user"""

    username = StringField("User Name",
                           validators=[InputRequired()])

    password = PasswordField("Password",
                           validators=[InputRequired()])

    email = StringField("Email Address",
                           validators=[InputRequired(), Email()])

    first_name = StringField("First Name",
                           validators=[InputRequired()])

    last_name = StringField("Last Name",
                           validators=[InputRequired()])

    #add in length constraints same as db constraints

class LoginForm(FlaskForm):
    """Form for logging in User"""

    username = StringField("User Name",
                           validators=[InputRequired()])

    password = PasswordField("Password",
                           validators=[InputRequired()])

class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""