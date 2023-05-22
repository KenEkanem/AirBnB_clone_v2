#!/usr/bin/python3
""" Module used to test the base model """

import os
import json
import unittest
import datetime
from models.base_model import BaseModel
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """ Test class for base model """

    def setUp(self):
        """ Set up test environment """
        self.name = 'BaseModel'

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def tearDown(self):
        """ Tear down test environment """
        try:
            os.remove('file.json')
        except Exception:
            pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_default(self):
        """ Test default initialization """
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_kwargs(self):
        """ Test initialization with kwargs """
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertIsNot(new, i)

    # Rest of the test cases...

if __name__ == "__main__":
    unittest.main()

