from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models.user import User
# from models.engine.storage import Storage
#
# storage = Storage()
# storage.reload()
from Clean_Blog import storage


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
        user = storage.query(User, 'username', username.data)
        if user:
            raise ValidationError('This username already exists')

    def validate_email(self, email):
        user = storage.query(User, 'email', email.data)
        if user:
            raise ValidationError('This email already exists')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
