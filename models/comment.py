#!/usr/bin/python3

"""
Comments Table for blog posts
"""
from Clean_Blog import db
from models.base_model import BaseModel, Column, Base, Integer, String
from models.user import User
from models.blog_post import BlogPost
from sqlalchemy import ForeignKey, Text


class Comment(BaseModel, db.Model):
    """
    Comments
    """

    __tablename__ = 'comments'
    post_id = db.Column(db.String(60), db.ForeignKey('blog_post.id'), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
