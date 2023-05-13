#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, String


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from .engine import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from .engine import FileStorage
    storage = FileStorage()
    storage.reload()
