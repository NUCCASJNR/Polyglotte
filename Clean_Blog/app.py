from flask import Flask, render_template, request, url_for
from forms import SignupForm, LoginForm
from flask_bcrypt import Bcrypt
from models import User
from storage import Storage

storage = Storage()

app = Flask(__name__)
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/signup')
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                    password=hashed_password)
        storage.new(user)
        storage.save()
    return render_template('signup.html', title='Sign Up', form=form)


if __name__ == '__main__':
    app.run(debug=True)
