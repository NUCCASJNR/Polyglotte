from flask import flash
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models.user import User
# from models import storage


class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3)],
                             render_kw={'placeholder': 'Enter your First Name'})
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3)],
                            render_kw={'placeholder': 'Enter your Last Name'})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'Enter a valid email address'})
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)],
                           render_kw={'placeholder': 'Choose a Username'})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)],
                             render_kw={'placeholder': 'Must be at least 8 characters'})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')],
                                     render_kw={'placeholder': 'Re-enter password'})
    submit = SubmitField('Get Started')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exists')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    picture = FileField(validators=[FileAllowed(['jpg', 'jpeg', 'png'])], render_kw={'style': 'display: none;'})
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                flash('{} already exists'.format(username.data), 'danger')
                raise ValidationError('This username already exists')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                flash('{} already exists'.format(email.data), 'danger')
                raise ValidationError('This email already exists')
