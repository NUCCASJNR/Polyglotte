from flask import redirect, url_for, render_template

from Clean_Blog import app, bcrypt
from Clean_Blog.forms import SignupForm, LoginForm
from models import User


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                    username=form.username.data, password=hashed_password)
        user.save()
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
    #                 username=form.username.data, password=hashed_password)
    #     user.save()
    #     return redirect(url_for('index'))
    return render_template('signin.html', title='Sign Up', form=form)

