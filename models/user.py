#!/usr/bin/python3
"""
Users module for the Blog
"""

from flask_login import UserMixin

from Clean_Blog import login_manager, db
from models.base_model import BaseModel


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


class User(BaseModel, db.Model, UserMixin):
    """
    The User class contains all the user's info
    """
    __tablename__ = 'users'
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    picture = db.Column(db.String(128), default='default.jpeg', nullable=False)
    bio = db.Column(db.Text)
    no_followers = db.Column(db.Integer, default=0)
    no_following = db.Column(db.Integer, default=0)
    blog_posts = db.relationship('BlogPost', back_populates='user', lazy=True)
    followers = db.relationship('Follower', back_populates='user')
    following = db.relationship('Following', back_populates='user')
    verified = db.Column(db.Boolean, nullable=False, default=False)
    verification_code = db.Column(db.String(60))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def increment_followers_count(self):
        """
        Increments the number of follower of a user by 1
        """
        self.no_followers += 1

    def increment_following_count(self):
        """
        Increments the number of users a user is following by 1
        """
        self.no_following += 1