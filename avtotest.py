import csv
import unittest
from pathlib import Path

from register import *


path = Path('.')


class FractionTest(unittest.TestCase):
    def test_read_csv(self):
        with open('users.csv', 'r') as file:
            reader = csv.DictReader(file)
        data = list(reader)
        assert type(data) == list
        assert all(isinstance(item, dict) for item in data)

    def test_get_user_input_login(self, test_login):
        test_login = "test_login"
        result = get_user_input()
        self.assertEqual(result['login'], 'test_login')

    def test_get_user_input_password(self, test_password):
        test_password = "test_password"
        result = get_user_input()
        self.assertEqual(result['password'], 'test_password')

    def test_get_user_input_email(self, test_email):
        test_email = "test_email"
        result = get_user_input()
        self.assertEqual(result['email'], 'test_email')

    def test_validate(self):
        valid_email = 'test@example.com'
        invalid_email = 'invalid@email'

        result = validate({'email': valid_email})
        self.assertTrue(result)

        result = validate({'email': invalid_email})
        self.assertFalse(result)
