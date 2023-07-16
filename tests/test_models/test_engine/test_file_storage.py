#!/usr/bin/python3
""" This module contains the Tests for FileStorage class
unittests:
    Test_FileStorage_Docs
    Test_FileStorage
"""

import unittest
import json
from models.base_model import BaseModel
from datetime import datetime
import inspect
from models.engine import file_storage
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
import os
import pep8

FileStorage = file_storage.FileStorage

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class Test_FileStorage_Docs(unittest.TestCase):
    """Tests the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Sets up the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_file_storage(self):
        """Tests that file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_file_storage(self):
        """Tests if test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Testing for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Testing for the FileStorage class docstrings """
        self.assertIsNot(FileStorage.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "State class needs a docstring")

    def test_fs_func_docstrings(self):
        """Tests for the presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class Test_FileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""
    def test_all_returns_dict(self):
        """Tests that 'all' returns the FileStorage.__objects attr"""
        storage = FileStorage()
        my_dict = storage.all()
        self.assertEqual(type(my_dict), dict)
        self.assertIs(my_dict, storage._FileStorage__objects)

    def test_new(self):
        """Tests that 'new' adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        new_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                new_dict[instance_key] = instance
                self.assertEqual(new_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save(self):
        """Tests if 'save' properly saves objects to file.json"""
        os.remove("file.json")
        storage = FileStorage()
        my_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            my_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = my_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in my_dict.items():
            my_dict[key] = value.to_dict()
        string = json.dumps(my_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
