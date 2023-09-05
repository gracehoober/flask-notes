from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import Email, Optional, InputRequired

class RegisterForm(FlaskForm):
    """Form for registering user"""

    username = StringField("User Name",
                           validators=[InputRequired()])

    password = StringField("Password",
                           validators=[InputRequired()])

    email = StringField("Email Address",
                           validators=[InputRequired(),Email()])

    first_name = StringField("First Name",
                           validators=[InputRequired()])

    last_name = StringField("Last Name",
                           validators=[InputRequired()])