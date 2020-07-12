#!/usr/bin/python3
""" Base Model Unit Test """
import unittest
import os
import pep8
from datetime import datetime
from models.base_model import BaseModel


class TestDocumentation(unittest.TestCase):
    """ Test BaseModel Documentation """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.base = BaseModel()
        cls.base.name = "Utest"
        cls.base.num = 77

    @classmethod
    def teardown(cls):
        """ Deletes instance after test """
        del cls.base

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """ Test docstring """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """ Test BaseModel methods """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """ Check BaseModel instance """
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save_BaseModel(self):
        """ Test BaseModel save function """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """ test BaseModel to dict function """
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


class TestBaseFunctionality(unittest.TestCase):
    """ Test file functionality """
    def setUp(self):
        """ Creates an instance before each test """
        self.test = BaseModel()

    def tearDown(self):
        """ Deletes instance after a test is finished """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_unique_id(self):
        """ Check if generates a UUID for every instance """
        test2 = BaseModel()
        self.assertNotEqual(self.test.id, test2.id)

    def test_creationat_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updatedat_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_save_function(self):
        """ Check if update works """
        toUpdate = self.test.updated_at
        self.test.save()
        self.assertNotEqual(toUpdate, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test),
                         "[BaseModel] ({}) {}".
                         format(self.test.id,
                                self.test.__dict__))

    def test_to_dict(self):
        """ Check dictionary function """
        dictionary = self.test.to_dict()
        self.assertEqual(type(dictionary), dict)
        self.assertTrue(hasattr(dictionary, '__class__'))
        self.assertEqual(type(dictionary['created_at']), str)
        self.assertEqual(type(dictionary['updated_at']), str)

    def test_kwargs(self):
        """ Send kwargs to instance """
        dictionary = self.test.to_dict()
        test2 = BaseModel(**dictionary)
        self.assertEqual(self.test.id,
                         test2.id)
        self.assertEqual(self.test.created_at,
                         test2.created_at)
        self.assertEqual(self.test.updated_at,
                         test2.updated_at)
        self.assertNotEqual(self.test, test2)


if __name__ == "__main__":
    unittest.main()
