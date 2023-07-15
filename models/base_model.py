#!/usr/bin/python3
""" A class BaseModel that defines all common attributes for other classes"""

from datetime import datetime
import uuid
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Base model class """
    def __init__(self, *args, **kwargs):
        """Initializes the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns a string representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with all keys/values of the instance"""
        _all = self.__dict__.copy()
        if "created_at" in _all:
            _all["created_at"] = _all["created_at"].strftime(time)
        if "updated_at" in _all:
            _all["updated_at"] = _all["updated_at"].strftime(time)
        _all["__class__"] = self.__class__.__name__
        return _all
