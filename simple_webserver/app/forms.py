from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', [DataRequired(), EqualTo('password')])  # This expects password2 ..
    submit = SubmitField('Register')

    def validate_username(self, username):
        u = User.query.filter_by(username=username.data).first()
        if u is not None:
            raise ValidationError('Please choose a different username')

    def validate_email(self, email):
        u = User.query.filter_by(email=email.data).first()
        if u is not None:
            raise ValidationError('Please choose a different email address')
