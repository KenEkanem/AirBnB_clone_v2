#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base
from models.review import Review


class User(BaseModel, Base):
    """
        This class defines, a user by various attributes SQLALCHEMY mapping
        This is the mapping mechanism(Instrumentation, of 'class' to 'table')
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', cascade='delete, all, delete-orphan',
                          backref='user')
    reviews = relationship('Review', cascade='all, delete, delete-orphan',
                           backref='user')