#!/usr/bin/python3
""" A class BaseModel that defines all common attributes for other classes"""
from datetime import datetime
import uuid
from . import storage

class BaseModel:
    """ Base model class """
    def __init__(self, *args, **kwargs):
        if kwargs:
            print("Not kwargs")
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key,  datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.now().isoformat()
        storage.save()
    def to_dict(self):
        _all = self.__dict__.copy()
        _all["__class__"] = type(self).__name__
        _all["created_at"] = self.created_at.isoformat()
        _all["updated_at"] = self.updated_at.isoformat()
        return _all


