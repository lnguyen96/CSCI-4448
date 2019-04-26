'''
This file handles all pages in which users enter in data, futhermore, this file has methods which validate their inputs
to ensure that the data exists within our database
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from travelapp.models import User, Car

# Used for validating user registration, queries database to ensure no duplicate usernames/emails
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

# Used to ensure necessary information is input when logging in
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# This class is used for when a user is adding a trip, mainly it's so that users select a car that we have information on
class Destination(FlaskForm):
    start = StringField('Start Location', validators=[DataRequired()])
    end = StringField('End Location', validators=[DataRequired()])
    year = IntegerField('Vehicle Year', validators=[DataRequired(), NumberRange(min=2009, message='The car is too old and unsafe to drive. Please use a differnt car')])
    make = StringField('Vehicle Make', validators=[DataRequired()])
    model = StringField('Vehicle Model', validators=[DataRequired()])
    submit = SubmitField('Enter')

    def validate_year(self, year):
        car = Car.query.filter_by(year=year.data).first()
        if not car:
            raise ValidationError('The car is too old and unsafe to drive. Please use a differnt car')

    def validate_make(self, make):
        car = Car.query.filter_by(make=make.data).first()
        if not car:
            raise ValidationError('There is no such make. Please check spelling')

    def validate_model(self, model):
        car = Car.query.filter_by(model=model.data).first()
        if not car:
            raise ValidationError('There is no such model. Please check spelling')