#!/usr/bin/python3
"""
This contains the unittests for class Amenity
Test classes:
    Test_Amenity_Docs
    Test_Amenity
"""

import unittest
from models import amenity
from models.base_model import BaseModel
from datetime import datetime
import inspect
import pep8

Amenity = amenity.Amenity


class Test_Amenity_Docs(unittest.TestCase):
    """ This checks the documentation and style of Amenity class """
    @classmethod
    def setUpClass(cls):
        """Setting up the doc tests"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """This tests if amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Checks whether test_amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """This tests for the amenity.py module docstrings"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Testing for the Amenity class docstrings"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """This tests for the presence of docstrings in Amenity methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class Test_Amenity(unittest.TestCase):
    """Testing the Amenity class"""
    def test_is_subclass(self):
        """This tests if Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Checks if Amenity has attribute name and if is an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """ Tests if to_dict method creates a dictionary with proper attrs"""
        am = Amenity()
        new_dict = am.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in am.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Testing if values in dict returned from to_dict are correct"""
        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        a = Amenity()
        new_d = a.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], a.created_at.strftime(time_fmt))
        self.assertEqual(new_d["updated_at"], a.updated_at.strftime(time_fmt))

    def test_str(self):
        """This tests if the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
