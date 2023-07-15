#!/usr/bin/python3
""" File storage Module """

import json
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place

classes = {"User": User, "BaseModel": BaseModel, "State": State,
           "Amenity": Amenity, "City": City, "Review": Review, "Place": Place}


class FileStorage:
    """ File storage class

    Serializes instances to a JSON file and deserializes JSON file to instances

    Attributes
    ----------
    __file_path: str
        defaults to file.json
    __objects: dict
        will store all objects by <class name>.id

    Methods
    -------
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """
        Parameters
        ----------
        obj: object
            object to save in __object
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """ Deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
