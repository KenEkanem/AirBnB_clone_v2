#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv

database = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade="all, delete-orphan", backref="state")

    if database != "db":
        @property
        def cities(self):
            """return a list City instances with state_id
            equals to the current State.id"""
            all_obj = models.storage.all()
            city_ins = []
            same_id = []
            for key in all_obj.keys():
                key_list = key.split('.')
                if key_list[0] == 'City':
                    city_ins.append(all_obj[key])
            for state in city_ins:
                if state.state_id == self.id:
                    same_id.append(state)
            return(same_id)
