#!/usr/bin/python3
"""
Users module for the Blog
"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, Column, String
from sqlalchmey import Text

class User(BaseModel, Base):
    """
    The User class contains all the user's info
    """
    __tablename__ = 'users'
    username = Column(string(60), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    first_name = Column(String(60), nullable=False)
    last_name = Column(string(60), nullable=False)
    profile_picture_url = Column(60)
    biography = Column(Text)
