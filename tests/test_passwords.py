import unittest
from app.models import User

class PasswordTests(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'wildcat')
        self.assertTrue(u.password_hash is not None)

    def test_password_getter(self):
        u = User(password = 'wildcat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'wildcat')
        self.assertTrue(u.verify_password('wildcat'))
        self.assertFalse(u.verify_password('husky'))

    def test_password_salts(self):
        u = User(password = 'wildcat')
        x = User(password = 'husky')
        self.assertTrue(u.password_hash != x.password_hash)
