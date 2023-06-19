#!/usr/bin/python3

"""
Comments Table for blog posts
"""

from models.base_model import BaseModel, Column, Base, Integer, String
from models.user import User
from models.blog_post import BlogPost
from sqlalchemy import ForeignKey, Text

class Comment(BaseModel, Base):
    """
    Comments
    """
    
    __tablename__ = 'comments'
    post_id = Column(String(60), ForeignKey('blog_post.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    content = Column(Text, nullable=False)
