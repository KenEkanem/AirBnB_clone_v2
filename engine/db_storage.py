#!/usr/bin/python3
"""Database storage engine"""
import os
from models.base_model import Base
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


class DBStorage:
    """database storage class"""
    __engine = None
    __session = None
    __session_factory = None

    db_objs = {"User": User, "Place": Place,
               "Amenity": Amenity, "State": State,
               "Review": Review, "City": City}

    def __init__(self):
        """initialization method"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(os.getenv("HBNB_MYSQL_USER"),
                                             os.getenv("HBNB_MYSQL_PWD"),
                                             os.getenv("HBNB_MYSQL_HOST"),
                                             os.getenv("HBNB_MYSQL_DB"),
                                             echo=True, pool_pre_pring=True))
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current databaase session for all objects"""
        entities = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = cls.__name__ + "." + str(obj.id)
                entities.update({key: obj})
            return (entities)
        else:
            for obj in self.db_objs.values():
                for ent_inst in self.__session.query(obj).all():
                    key = "{}.{}".format(obj.__name__, ent_inst.id)
                    entities.update({key: ent_inst})
            return (entities)

    def new(self, obj):
        """add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current session if obj is not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all database with the metadata"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session_factory = scoped_session(Session)
        self.__session = self.__session_factory()

    def close(self):
        """close the session object"""
        self.__session_factory.remove()
