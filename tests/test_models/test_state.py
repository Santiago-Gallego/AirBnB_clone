#!/usr/bin/python3
""" State Model Unit Test """
import unittest
import os
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestDocumentation(unittest.TestCase):
    """ Test State Documentation """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.state = State()
        cls.state.name = "Jericho"

    @classmethod
    def teardown(cls):
        """ Deletes instance after test """
        del cls.state

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_State(self):
        """ Test docstring """
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """ Test Amenity attributes """
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """ Test State subclass """
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """ Test attribute State type  """
        self.assertEqual(type(self.state.name), str)

    def test_save_State(self):
        """ Test save """
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """ Test to dict """
        self.assertEqual('to_dict' in dir(self.state), True)


class TestState(unittest.TestCase):
    """ Test state """
    def setUp(self):
        """ Creates an instance before each test """
        self.test = State()

    def tearDown(self):
        """ Deletes instance after a test """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_unique_id(self):
        """ Check if generates a UUID for every instance """
        test2 = State()
        self.assertNotEqual(self.test.id, test2.id)

    def test_created_at_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updated_at_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_name_type(self):
        """ Check state name type """
        self.assertEqual(type(State.name), str)

    def test_save(self):
        """ Test save function """
        check = self.test.updated_at
        self.test.save()
        self.assertNotEqual(check, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test),
                         "[State] ({}) {}".
                         format(self.test.id,
                                self.test.__dict__))

    def test_dictionary(self):
        """ Check to_dict function """
        dictionary = self.test.to_dict()
        self.assertEqual(type(dictionary), dict)
        self.assertTrue(hasattr(dictionary, '__class__'))
        self.assertEqual(type(dictionary['created_at']), str)
        self.assertEqual(type(dictionary['updated_at']), str)

    def test_kwargs(self):
        """ Validate kawrgs arguments """
        dictionary = self.test.to_dict()
        test2 = State(**dictionary)
        self.assertEqual(self.test.id, test2.id)
        self.assertEqual(self.test.created_at, test2.created_at)
        self.assertEqual(self.test.updated_at, test2.updated_at)
        self.assertNotEqual(self.test, test2)


if __name__ == "__main__":
    unittest.main()
