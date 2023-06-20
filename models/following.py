#!/usr/bin/python3

"""
This module handles the no of users a user is following
"""

from sqlalchemy import ForeignKey

from models.base_model import Base, BaseModel, Column, Integer, String
from models.user import User, relationship


class Following(BaseModel, Base):
    """
    Followers class
    """
    __tablename__ = 'following'
    follower_user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='following')