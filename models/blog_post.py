#!/usr/bin/python3

"""
This module handles info about a specific blog post
"""

from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Column, String, Base, Integer
from sqlalchemy import ForeignKey, Text
from models.user import User

class BlogPost(BaseModel, Base):
    """
    Blog post Class for all blog posts
    """
    __tablename__ = 'blog_post'
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    likes_count = Column(Integer)
    views_count = Column(Integer)
    user = relationship('User', back_populates='blog_posts')
