#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base, Column
from models import relationship, String
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    else:
        """if the datatype storage is not database"""
        @property
        def cities(self):
            """import models module"""
            import models
            from models.city import City

            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
