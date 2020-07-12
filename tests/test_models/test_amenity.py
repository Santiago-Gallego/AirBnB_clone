#!/usr/bin/python3
""" Amenity Model Unit Test """
import unittest
import os
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestDocumentation(unittest.TestCase):
    """ Test Amenity Documentation """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.amenity = Amenity()
        cls.amenity.name = "Utest"

    @classmethod
    def teardown(cls):
        """ Deletes instance after test """
        del cls.amenity

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Amenity(self):
        """ Test docstring """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """ Test Amenity attributes """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """ Test Amenity subclass """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """ Test Amenity types """
        self.assertEqual(type(self.amenity.name), str)

    def test_save_Amenity(self):
        """ Test save """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """ Test to dict """
        self.assertEqual('to_dict' in dir(self.amenity), True)


class TestAmenityFunctionality(unittest.TestCase):
    """ Test amenity """
    def setUp(self):
        """ Creates an instance before each test """
        self.test = Amenity()

    def tearDown(self):
        """ Deletes instance after test """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_unique_id(self):
        """ Check if generates a UUID for every instance """
        test2 = Amenity()
        self.assertNotEqual(self.test.id, test2.id)

    def test_created_at_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updated_at_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_amenity_type(self):
        """ Check amenity type """
        self.assertEqual(type(Amenity.name), str)

    def test_save(self):
        """ Test save function """
        check = self.test.updated_at
        self.test.save()
        self.assertNotEqual(check, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test),
                         "[Amenity] ({}) {}".
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
        test2 = Amenity(**dictionary)
        self.assertEqual(self.test.id, test2.id)
        self.assertEqual(self.test.created_at, test2.created_at)
        self.assertEqual(self.test.updated_at, test2.updated_at)
        self.assertNotEqual(self.test, test2)


if __name__ == "__main__":
    unittest.main()
