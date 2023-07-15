#!/usr/bin/python
""" This defines class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This represents Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of Amenity """
        super().__init__(*args, **kwargs)
