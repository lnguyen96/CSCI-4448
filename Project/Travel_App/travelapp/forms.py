from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from travelapp.models import User


class registerform(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    passwordconfirmed = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
    	user = User.query.filter_by(username = username.data).first()
    	if user:
    		raise ValidationError("Username is not available")

    def validate_email(self, email):
    	user = User.query.filter_by(email = email.data).first()
    	if user:
    		raise ValidationError("Email is taken")


class loginform(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("Login")
    remembered = BooleanField("Remember Me")
