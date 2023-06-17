#!/usr/bin/python3

"""
Comments Table for blog posts
"""

from models.base_model import BaseModel, Base, Integer, String
from models.user import User
from models.blog_post import BlogPost

class Comment(BaseModel, Base):
    """
    Comments
    """
    
    __tablename__ = 'comments'
    post_id = Column(Integer, ForeignKey('blog_post.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(Text)