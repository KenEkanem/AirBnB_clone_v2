#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime(), nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if key == 'updated_at':
                    kwargs['updated_at'] = \
                            datetime.strptime(kwargs['updated_at'],
                                              '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'created_at':
                    kwargs['created_at'] = \
                            datetime.strptime(kwargs['created_at'],
                                              '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        copy_dict = self.__dict__.copy()
        if "_sa_instance_state" in copy_dict:
            del copy_dict["_sa_instance_state"]
        return '[{}] ({}) {}'.format(cls, self.id, copy_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        models.storage.new(self)
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' not in dictionary:
            return dictionary
        else:
            del dictionary['_sa_instance_state']
            return dictionary

    def delete(self):
        """delete current instance from the storage by calling\
                the delete method"""
        models.storage.delete(self)
