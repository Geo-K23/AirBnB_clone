#!/usr/bin/python
""" This holds class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This represents a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialization of user"""
        super().__init__(*args, **kwargs)
