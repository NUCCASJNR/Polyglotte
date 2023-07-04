#!/usr/bin/python3

"""
This module handles info about a specific blog post
"""

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship

from Clean_Blog import db
from models.base_model import Base, BaseModel, Column, Integer, String
from models.user import User


class BlogPost(BaseModel, db.Model):
    """
    Blog post Class for all blog posts
    """
    __tablename__ = 'blog_post'
    user_id = db.Column(db.String(60), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    likes_count = db.Column(db.Integer)
    views_count = db.Column(db.Integer)
    picture = db.Column(db.String(256))
    user = db.relationship('User', back_populates='blog_posts')
    category = db.Column(db.String(60))

    def increment_likes(self):
        """
        Adds a new like to a blog post
        """
        self.likes_count += 1

    def increment_views(self):
        """
        Adds a New View to a Blog Post
        """
        self.views_count += 1
