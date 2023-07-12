#!/usr/bin/python3
"""This module tests the file storage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class FileStorageTest(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        storage = FileStorage()
    def test_all(self):
        results = storage.all()
