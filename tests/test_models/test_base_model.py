#!/usr/bin/python3
""" Base model unittest """
import unittest
from  models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new_obj = BaseModel()
    def test_id(self):
        self.assertIsInstance(self.new_obj.id, str)
    def test_instance_class(self):
        new_obj = BaseModel()
        self.assertIsInstance(self.new_obj, BaseModel)
if __name__ == "__main__":
    unittest.main()

