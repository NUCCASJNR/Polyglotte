from flask import flash
from flask_ckeditor import CKEditorField
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models.user import User
# from models import storage


class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3)],
                             render_kw={'placeholder': 'John'})
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3)],
                            render_kw={'placeholder': 'Doe'})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'johndoe123@email.com'})
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)],
                           render_kw={'placeholder': 'jondoe123'})
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
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)],
                           render_kw={'placeholder': 'Enter your username'})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)],
                             render_kw={'placeholder': 'Enter your password'})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class VerifyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={'placeholder': 'Enter your email address'})
    verification_code = StringField('Verification Code', validators=[DataRequired()], render_kw={'placeholder': 'Enter the verification code'})
    submit = SubmitField('Verify')

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


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subheading = StringField('Sub-Heading', validators=[DataRequired()])
    category = StringField('Category')
    # content = TextAreaField('Content', validators=[DataRequired()], render_kw={'placeholder': 'Content', 'rows': '8'})
    content = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
