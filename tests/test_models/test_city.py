#!/usr/bin/python3
""" City Model Unit Test """
import unittest
import os
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestDocumentation(unittest.TestCase):
    """ Test Amenity Documentation """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.city = City()
        cls.city.name = "Jericho"
        cls.city.state_id = "Russia"

    @classmethod
    def teardown(cls):
        """ Deletes instance after test """
        del cls.city

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """ Test docstring """
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """chekcing if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """ Check if City is Basemodel subclass """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """ Test save """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """ test if the save works """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """ Test to dict """
        self.assertEqual('to_dict' in dir(self.city), True)


class TestCityModel(unittest.TestCase):
    """ Test City """
    def setUp(self):
        """ Creates an instance before each test """
        self.test = City()

    def tearDown(self):
        """ Deletes instance after a test """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_unique_id(self):
        """ Check if generates a UUID for every instance """
        test2 = City()
        self.assertNotEqual(self.test.id, test2.id)

    def test_created_at_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updated_at_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_city_type(self):
        """ Check city type """
        self.assertEqual(type(City.name), str)

    def test_state_id_type(self):
        """ Check state_id type """
        self.assertEqual(type(City.state_id), str)

    def test_save(self):
        """ Test save function """
        check = self.test.updated_at
        self.test.save()
        self.assertNotEqual(check, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test),
                         "[City] ({}) {}".
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
        test2 = City(**dictionary)
        self.assertEqual(self.test.id, test2.id)
        self.assertEqual(self.test.created_at, test2.created_at)
        self.assertEqual(self.test.updated_at, test2.updated_at)
        self.assertNotEqual(self.test, test2)


if __name__ == "__main__":
    unittest.main()
