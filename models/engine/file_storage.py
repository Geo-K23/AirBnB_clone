#!/usr/bin/python3
""" File storage Module """

import json
import os

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
        _key = obj.__class__.__name__ + "." + obj.id
        type(self).__objects[_key] = obj.to_dict()
    def save(self):
       """ serializes __objects to the JSON file (path: __file_path)"""
       with open(type(self).__file_path, "w") as f:
           json.dump(type(self).__objects, f)
    def reload(self):
        """ Deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists ; otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised)
        """
        if os.path.isfile(self.__file_path):
            with open(type(self).__file_path, "r") as f:
                type(self).__objects = json.load(f)
