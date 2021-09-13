#!/usr/bin/python3
""" State Module for HBNB project """
# from _typeshed import Self
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from os import getenv
# parent


class State(BaseModel, Base):
    """ State class """

    storage_type = getenv('HBNB_TYPE_STORAGE')
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        # cities -> nombre de la tabla en la clase hija(City)
        # back_populate -> nombre de la variable que recibe la relacion en city
        # cascade -> borra los registros vinculados a State en City
        cities = relationship('City', back_populates='state',
                              cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            """returns a list of City instaces"""
            from models import storage
            from models.city import City
            # dictionary of objects of City CLass
            dict_ = storage.all(City)
            # list de ciudades que contiene el state_id == Satae.id
            list_ = []
            for v in dict_.values():
                # v es un objeto, porlo tanto debemos acceder
                # a los valores de su dccionario
                if self.id in v.__dict__.values():
                    list_.append(v)
            return list_
