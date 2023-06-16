#!/usr/bin/python3

"""
This module handles info about a specific blog post
"""

from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Column, String, Base, Integer
from sqlalchemy import ForeignKey
from models.users import User

class BlogPost(BaseModel, Base):
    """
    Blog post Class for all blog posts
    """
    __tablename__ = 'blog_post'
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    likes_count = Column(Integer)
    views_count = Column(Integer)
