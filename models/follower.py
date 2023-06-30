#!/usr/bin/python3

"""
This module handles the followers of a particular User
"""

from sqlalchemy import ForeignKey

from Clean_Blog import db
from models.base_model import Base, BaseModel, Column, Integer, String
from models.user import User, relationship


class Follower(BaseModel, db.Model):
    """
    Followers class
    """
    __tablename__ = 'followers'
    followed_user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False, unique=True)
    user = db.relationship('User', back_populates='followers')
