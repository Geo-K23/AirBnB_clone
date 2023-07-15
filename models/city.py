#!/usr/bin/python
""" This defines the class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """This is a representation of a city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of a city"""
        super().__init__(*args, **kwargs)
