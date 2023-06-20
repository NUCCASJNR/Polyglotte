#!/usr/bin/python3

"""
This module handles the followers of a particular User
"""

from models.base_model import BaseModel, Base, Integer, Column, String
from models.user import User, relationship
from sqlalchemy import ForeignKey

class Follower(BaseModel, Base):
    """
    Followers class
    """
    __tablename__ = 'followers'
    followed_user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='followers')