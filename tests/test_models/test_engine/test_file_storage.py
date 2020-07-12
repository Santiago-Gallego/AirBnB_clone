#!/usr/bin/python3
""" FileStorage Unit Test """
import unittest
import models
import pep8
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorageDocumentation(unittest.TestCase):
    """ Test FileStorage Documentation """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.user = User()
        cls.user.first_name = "Test"
        cls.user.last_name = "unit"
        cls.user.email = "123@test.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """ Deletes instance after test """
        del cls.user

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """ tests all FileStorage function """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """ Test new FileStorage function """
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 12345
        user.name = "Test"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """ Test reload FileStorage function """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

    def test_pep8_FileStorage(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
