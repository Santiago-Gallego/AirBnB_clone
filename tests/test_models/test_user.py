#!/usr/bin/python3
""" User Model Unit Test """
import unittest
import os
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestDocumentation(unittest.TestCase):
    """ Test User Documentation """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.user = User()
        cls.user.first_name = "Test"
        cls.user.last_name = "Unit"
        cls.user.email = "123@test.com"
        cls.user.password = "jericho"

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

    def test_pep8_User(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_User(self):
        """ Test docstring """
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """ Test User attributes """
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """ Test if User is Basemodel subclass """
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_User(self):
        """ Test attribute User type """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save_User(self):
        """ Test save """
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """ Test to dict """
        self.assertEqual('to_dict' in dir(self.user), True)


class TestUserModel(unittest.TestCase):
    """ Test User """
    def setUp(self):
        """ Creates an instance before each test """
        self.test = User()

    def tearDown(self):
        """ Deletes instance after a test """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_unique_id(self):
        """ Check if generates a UUID for every instance """
        test2 = User()
        self.assertNotEqual(self.test.id, test2.id)

    def test_created_at_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updated_at_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_email_type(self):
        """ Test email type """
        self.assertEqual(type(User.email), str)

    def test_password_type(self):
        """ Check password type """
        self.assertEqual(type(User.password), str)

    def test_first_name_type(self):
        """ Check first name type """
        self.assertEqual(type(User.first_name), str)

    def test_last_name_type(self):
        """ Check last name type """
        self.assertEqual(type(User.last_name), str)

    def test_save(self):
        """ Test save function """
        check = self.test.updated_at
        self.test.save()
        self.assertNotEqual(check, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test),
                         "[User] ({}) {}".
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
        test2 = User(**dictionary)
        self.assertEqual(self.test.id, test2.id)
        self.assertEqual(self.test.created_at, test2.created_at)
        self.assertEqual(self.test.updated_at, test2.updated_at)
        self.assertNotEqual(self.test, test2)


if __name__ == "__main__":
    unittest.main()
