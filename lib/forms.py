from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, Regexp, Email


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[
        InputRequired(),
        Regexp(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[^a-zA-Z0-9]).*$',
               message="Password must contain at least 1 UpperCase, 1 Number, and 1 special character"),
        Length(min=8)
    ], render_kw={"placeholder": "Password"})
    email = EmailField(validators=[InputRequired(), Length(min=8, max=100)], render_kw={"placeholder": "Email"})
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')
