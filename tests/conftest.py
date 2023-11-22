from project_encryption.src.cipher import Cipher, EnteredZeroStep, EnteredNegativeStep, EnteredStepMoreThanAlphabet
import pytest

@pytest.fixture
def encrypt_test_data():
    return [
        ('cat', 3, 'fdw'),
        ('cat', 5, 'hfy'),
        ('hello', 3, 'khoor'),
        ('hello', 5, 'mjqqt'),
    ]
