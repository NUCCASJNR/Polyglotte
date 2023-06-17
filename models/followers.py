#!/usr/bin/python3

"""
This module handles the followers of a particular User
"""

from models.base_model import BaseModel, Integer, Column
from models.user import User
from sqlalchemy import ForeignKey

class Followers(BaseModel, Base):
    """
    Followers class
    """
    follower_user_id = Column(Integer, ForeignKey('user.id'))
