#!/usr/bin/python
""" This is a Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initialization of Review"""
        super().__init__(*args, **kwargs)
