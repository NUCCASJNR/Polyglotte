import os.path
import secrets
import requests
from PIL import Image
from models import User, BlogPost
from flask import redirect, url_for, render_template, request, flash, abort
from flask_login import login_user, current_user, logout_user, login_required
from Clean_Blog import app, bcrypt, db
from Clean_Blog.forms import SignupForm, LoginForm, UpdateForm, PostForm, VerifyForm


# from models import storage


@app.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('index.html', posts=posts)



def send_verification_email(email, verification_code):
    api_key = os.environ.get('elastic_API')
    url = 'https://api.elasticemail.com/v2/email/send'
    payload = {
        'apikey': api_key,
        'from': 'polyglotte@polyglotte.tech',
        'to': email,
        'subject': 'Account Verification',
        'bodyHtml': f'Your verification code is: {verification_code}',
        'isTransactional': False
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return True
    return False

def generate_verification_code():
    import secrets
    verification_code = secrets.token_hex(3)
    return verification_code
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        verification_code = generate_verification_code()
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            username=form.username.data,
            password=hashed_password,
            verification_code=verification_code 
        )
        db.session.add(user)
        db.session.commit()
        send_verification_email(user.email, verification_code)

        flash('Your account has been created. Check your email for verification instructions', 'success')
        return redirect(url_for('verify'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = VerifyForm()
    if form.validate_on_submit():
        email = form.email.data
        verification_code = form.verification_code.data

        user = User.query.filter_by(email=email).first()
        if user and user.verification_code == verification_code:
            # Verification successful
            user.verified = True
            db.session.commit()
            login_user(user)  # Log in the user
            flash('Your account has been verified and you have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            # Verification failed
            flash('Invalid verification code. Please try again.', 'danger')
    return render_template('verify.html', title='Account Verification', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if user.verified:
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                flash('You have been logged in!', 'success')
                return redirect(next_page) if next_page else redirect(url_for('index'))
            flash('Please verify your email address to log in.', 'info')
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('signin.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_extension
    picture_path = os.path.join(app.root_path, 'static/img/profile_pics', picture_filename)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.picture = picture_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has successfully been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.username.data = current_user.username
        form.email.data = current_user.email
    if not current_user.verified:
            flash('Please verify your email address to access your account.', 'info')
    image_file = url_for('static', filename='img/profile_pics/{}'.format(current_user.picture))
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).filter_by(user=current_user).all()
    return render_template('profile_page.html', form=form, image_file=image_file, posts=posts)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.category.data == '':
            form.category.data = 'Miscellaneous'
        post = BlogPost(title=form.title.data, content=form.content.data, subheading=form.subheading.data,
                        category=form.category.data, user=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@app.route('/post/<string:post_id>')
def show_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    post_picture = url_for('static', filename='img/{}'.format(post.picture))
    return render_template('post_page.html', title=post.title, post=post, picture=post_picture)


@app.route('/post/<string:post_id>/update', methods=['POST', 'GET'])
@login_required
def update_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.subheading = form.subheading.data
        post.category = form.category.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('show_post', post_id=post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.subheading.data = post.subheading
        form.category.data = post.category
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route('/post/<string:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('index'))


@app.route('/post')
def post():
    return render_template('post_page.html')
