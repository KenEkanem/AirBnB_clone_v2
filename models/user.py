#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import BaseModel, Base, Column
from models import String, relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", back_populates="user")
        reviews = relationship("Review", back_populates="user")
