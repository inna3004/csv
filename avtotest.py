import unittest
from pathlib import Path
import pytest

from register import validate_1, validate_2
from register import logining
path = Path('.')


class RegistrationTest(unittest.TestCase):


    def test_logining():
        test_data = {
            "login": "test_user",
            "password": "123456"
        }

        result = logining(test_data)

        assert result is True


    def test_validate_1(self):
        valid_email = 'test@example.com'
        invalid_email = 'invalid@email'

        result = validate_1({'email': valid_email})
        self.assertTrue(result)

        result = validate_1({'email': invalid_email})
        self.assertFalse(result)


def test_validate_2():
    test_data = {
        "login": "test_user",
        "email": "test@example.com"
    }

    with pytest.raises(Exception) as excinfo:
        validate_2(test_data)

    assert "Такой пользователь уже существует." in str(excinfo.value)