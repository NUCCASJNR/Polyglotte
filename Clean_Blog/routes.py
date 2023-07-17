import os.path
import secrets
from PIL import Image
from models import User, BlogPost
from flask import redirect, url_for, render_template, request, flash, abort
from flask_login import login_user, current_user, logout_user, login_required
from Clean_Blog import app, bcrypt, db
from Clean_Blog.forms import SignupForm, LoginForm, UpdateForm, PostForm, BioForm


# from models import storage


@app.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('index.html', posts=posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                    username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You can now login', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You have been logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('signin.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


def save_picture_profile(form_picture):
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
    bio_form = BioForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture_profile(form.picture.data)
            current_user.picture = picture_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has successfully been updated', 'success')
        return redirect(url_for('account'))
    if bio_form.validate_on_submit():
        current_user.bio = bio_form.bio.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.username.data = current_user.username
        form.email.data = current_user.email
        bio_form.bio.data = current_user.bio
    image_file = url_for('static', filename='img/profile_pics/{}'.format(current_user.picture))
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).filter_by(user=current_user).all()
    return render_template('profile_page.html', form=form, bio_form=bio_form, image_file=image_file, posts=posts)


def save_picture_blog(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_extension
    picture_path = os.path.join(app.root_path, 'static/img/blog_pics', picture_filename)
    output_size = (960, 540)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.category.data == '':
            form.category.data = 'Miscellaneous'
        if form.picture.data:
            picture_filename = save_picture_blog(form.picture.data)
        else:
            picture_filename = None
        post = BlogPost(title=form.title.data, content=form.content.data, subheading=form.subheading.data,
                        category=form.category.data, picture=picture_filename, user=current_user)

        db.session.add(post)
        db.session.commit()

        flash('Your post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@app.route('/post/<string:post_id>')
def show_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    post_picture = url_for('static', filename='img/blog_pics/{}'.format(post.picture))
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
        if form.picture.data:
            picture_filename = save_picture_blog(form.picture.data)
            post.picture = picture_filename
        else:
            post.picture = 'default_post.jpg'
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('show_post', post_id=post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.subheading.data = post.subheading
        form.category.data = post.category
        form.content.data = post.content
        form.picture.data = post.picture
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
