#!/usr/bin/python3

"""
This module handles info about a specific blog post
"""

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel, Column, Integer, String
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
    picture = Column(String(256))
    user = relationship('User', back_populates='blog_posts')
    category = Column(String(60), nullable=False)

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