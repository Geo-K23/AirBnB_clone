#!/usr/bin/python3
"""This defines the class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is a representation a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
