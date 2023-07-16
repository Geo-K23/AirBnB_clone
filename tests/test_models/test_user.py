#!/usr/bin/python3
"""
This contains the tests for implementation & docstrings for class User

Test classe:
    Test_UserDocs()
    Test_User()
"""

import unittest
from models import user
from models.base_model import BaseModel
from datetime import datetime
import pep8
import inspect

User = user.User


class Test_UserDocs(unittest.TestCase):
    """This checks the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """This sets up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """This tests that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """This checks that tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Tests for the user.py module docstrings"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the User class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Testing for the presence of docstrings in User methods """
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class Test_User(unittest.TestCase):
    """ Testing for the User class"""
    def test_is_subclass(self):
        """This tests that User is a subclass of BaseModel """
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "created_at"))

    def test_first_name_attr(self):
        """Test that User has first_name attr and is an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """This tests for User last_name attr & if it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_email_attr(self):
        """Test that User has email attr and is an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password_attr(self):
        """Test that User has password attr and is an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_to_dict_creates_dict(self):
        """Checks if to_dict method creates a dictionary with proper attrs"""
        u = User()
        my_dict = u.to_dict()
        self.assertEqual(type(my_dict), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in my_dict)
            self.assertTrue("__class__" in my_dict)

    def test_to_dict_values(self):
        """This tests that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        newD = u.to_dict()
        self.assertEqual(newD["__class__"], "User")
        self.assertEqual(type(newD["created_at"]), str)
        self.assertEqual(type(newD["updated_at"]), str)
        self.assertEqual(newD["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(newD["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """Testing that the str method has the correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
