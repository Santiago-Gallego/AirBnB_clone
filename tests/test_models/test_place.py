#!/usr/bin/python3
""" Place Model Unit Test """
import unittest
import os
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestDocumentation(unittest.TestCase):
    """ Test Place Documentation """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.place = Place()
        cls.place.city_id = "test-123"
        cls.place.user_id = "987-unit"
        cls.place.name = "jerico"
        cls.place.description = "Paradise"
        cls.place.number_rooms = 10000000
        cls.place.number_bathrooms = 7
        cls.place.max_guest = 10000000
        cls.place.price_by_night = 77
        cls.place.latitude = 160.0
        cls.place.longitude = 120.0
        cls.place.amenity_ids = ["123-unittest"]

    @classmethod
    def teardown(cls):
        """ Deletes instance after test """
        del cls.place

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Place(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Place(self):
        """ Test docstring """
        self.assertIsNotNone(Place.__doc__)

    def test_attributes_Place(self):
        """ Test Amenity attributes """
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_is_subclass_Place(self):
        """ Test if Place is Basemodel subclass """
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attribute_types_Place(self):
        """ Test attribute Place type """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_save_Place(self):
        """ Test save """
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_Place(self):
        """ Test to dict """
        self.assertEqual('to_dict' in dir(self.place), True)


class TestPlace(unittest.TestCase):
    """Testing Place"""
    def setUp(self):
        """ Creates an instance before each test """
        self.test = Place()

    def tearDown(self):
        """ Deletes instance after a test """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_uniqueUUID(self):
        """ Check if generates a UUID for every instance """
        test2 = Place()
        self.assertNotEqual(self.test.id, test2.id)

    def test_created_at_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updated_at_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is str data type
        """
        self.assertEqual(type(Place.name), str)

    def test_city_id(self):
        """ Test city-id type """
        self.assertEqual(type(Place.city_id), str)

    def test_user_id(self):
        """ Test user_id type """
        self.assertEqual(type(Place.user_id), str)

    def test_description(self):
        """ Test description type """
        self.assertEqual(type(Place.description), str)

    def test_number_rooms(self):
        """ Test number_rooms type """
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test number_bathrooms type """
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        """ Test max_guest type """
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night(self):
        """ Test price by nigth type """
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitutde(self):
        """ Test latitude type """
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        """ Test longitude type """
        self.assertEqual(type(Place.longitude), float)

    def test_amenity_ids(self):
        """ Check amenity_ids type """
        self.assertEqual(type(Place.amenity_ids), list)

    def test_save(self):
        """ Test save function """
        check = self.test.updated_at
        self.test.save()
        self.assertNotEqual(check, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test), "[Place] ({}) {}".
                         format(self.test.id, self.test.__dict__))

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
        test2 = Place(**dictionary)
        self.assertEqual(self.test.id, test2.id)
        self.assertEqual(self.test.created_at, test2.created_at)
        self.assertEqual(self.test.updated_at, test2.updated_at)
        self.assertNotEqual(self.test, test2)


if __name__ == "__main__":
    unittest.main()
