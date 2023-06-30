#!/usr/bin/python3

"""
This module handles the no of users a user is following
"""

from sqlalchemy import ForeignKey

from Clean_Blog import db
from models.base_model import Base, BaseModel, Column, Integer, String
from models.user import User, relationship


class Following(BaseModel, db.Model):
    """
    Followers class
    """
    __tablename__ = 'following'
    follower_user_id = db.Column(String(60), db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='following')
