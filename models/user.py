#!/usr/bin/python3
"""
Users module for the Blog
"""

from models.base_model import BaseModel, Base, Column, String, Integer
from sqlalchemy import Text
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    The User class contains all the user's info
    """
    __tablename__ = 'users'
    username = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    picture = Column(String(128))
    bio = Column(Text)
    no_followers = Column(Integer, default=0)
    no_following = Column(Integer, default=0)
    blog_posts = relationship('BlogPost', back_populates='user')
    followers = relationship('Follower', back_populates='user')
    following = relationship('Following', back_populates='user')

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