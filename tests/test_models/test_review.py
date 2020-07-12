#!/usr/bin/python3
""" Review Model Unit Test """
import unittest
import os
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestDocumentation(unittest.TestCase):
    """ Test Review Documentation """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.rev = Review()
        cls.rev.place_id = "123-test"
        cls.rev.user_id = "987-unit"
        cls.rev.text = "Just jericho"

    @classmethod
    def teardown(cls):
        """ Deletes instance after test """
        del cls.rev

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Review(self):
        """ Test docstring """
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """ Test Review attributes """
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """ Test if review is BaseModel subclass """
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """ Test Review types """
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    def test_save_Review(self):
        """ Test save """
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """ Test to dict """
        self.assertEqual('to_dict' in dir(self.rev), True)


class TestReviewModel(unittest.TestCase):
    """ Test review """
    def setUp(self):
        """ Creates an instance before each test """
        self.test = Review()

    def tearDown(self):
        """ Deletes instance after a test """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_unique_id(self):
        """ Check if generates a UUID for every instance """
        test2 = Review()
        self.assertNotEqual(self.test.id, test2.id)

    def test_created_at_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updated_at_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_place_id(self):
        """ Test place_id type """
        self.assertEqual(type(Review.place_id), str)

    def test_user_id(self):
        """ Test user_id type """
        self.assertEqual(type(Review.user_id), str)

    def test_text(self):
        """ Test review text type """
        self.assertEqual(type(Review.text), str)

    def test_save(self):
        """ Test save function """
        check = self.test.updated_at
        self.test.save()
        self.assertNotEqual(check, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test),
                         "[Review] ({}) {}".
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
        test2 = Review(**dictionary)
        self.assertEqual(self.test.id, test2.id)
        self.assertEqual(self.test.created_at, test2.created_at)
        self.assertEqual(self.test.updated_at, test2.updated_at)
        self.assertNotEqual(self.test, test2)


if __name__ == "__main__":
    unittest.main()
