#!/usr/bin/python3

"""
This module handles the followers of a particular User
"""

from models.base_model import BaseModel, Base, Integer, Column
from models.user import User
from sqlalchemy import ForeignKey

class Follower(BaseModel, Base):
    """
    Followers class
    """
    __tablename__ = 'followers'
    follower_user_id = Column(Integer, ForeignKey('user.id'))
