#!/usr/bin/python3
"""adding a database"""

from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""
get database details stored in environment variables
"""
user = getenv("HBNB_MYSQL_USER")
passwd = getenv("HBNB_MYSQL_PWD")
db = getenv("HBNB_MYSQL_DB")
host = getenv("HBNB_MYSQL_HOST")
env = getenv("HBNB_MYSQL_HOST")


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """creating a connection"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format
                                      (user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """query"""
        diction = dict()
        if cls is not None:
            cls = eval(cls)
            obj_ins = self.__session.query(cls).all()
            for obj in obj_ins:
                key = '.'.join([obj.__class__.__name__, obj.id])
                diction[key] = obj
        else:
            all_cls = [BaseModel, User, State, City, Amenity, Place, Review]
            for cls in all_cls:
                obj_ins = self.__session.query(cls).all()
                for obj in obj_ins():
                    key = '.'.join([obj.__class__.__name__, obj.id])
                    diction[key] = obj
        return (diction)

    def new(self, obj):
        """add changes"""
        self.__session.add(obj)

    def save(self):
        """commit session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates tables and session"""
        Base.metadata.create_all(self.__engine)
        ses_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_factory)
        self.__session = Session

    def close(self):
        """calls remove()(sqlalchemy) on __session"""
        self.__session.remove()
