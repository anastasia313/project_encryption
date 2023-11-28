from src.cipher import Cipher, EnteredZeroStep, EnteredNegativeStep, EnteredStepMoreThanAlphabet
import pytest


@pytest.mark.parametrize(
    "txt, step, expected_result",
    [
        ('cat', 3, 'zxq'),
        ('cat', 5, 'xvo'),
        ('hello', 3, 'ebiil'),
        ('hello', 5, 'czggj'),
    ]
)
def test_decrypt_lowercase(txt, step, expected_result):
    cipher = Cipher()
    result = cipher.encrypt(txt, step)
    assert result == expected_result

@pytest.mark.parametrize(
    "txt, step, expected_result",
    [
        ('Cat', 3, 'Zxq'),
        ('CAT', 5, 'XVO'),
        ('hellO', 3, 'ebiiL'),
        ('HELLO', 5, 'CZGGJ')
    ]
)
def test_decrypt_uppercase(txt, step, expected_result):
    cipher = Cipher()
    result = cipher.encrypt(txt, step)
    assert result == expected_result

@pytest.mark.parametrize(
    "txt, step, expected_result",
    [
        ('456', 3, '123'),
        ('789', 3, '456')
    ]
)
def test_decrypt_digits(txt, step, expected_result):
    cipher = Cipher()
    result = cipher.encrypt(txt, step)
    assert result == expected_result

def test_decrypt_limit_digits_for_value_1():
    txt = '1'
    step = 3
    expected_result = '8'
    cipher = Cipher()
    result = cipher.encrypt(txt, step)
    assert result == expected_result

@pytest.mark.parametrize(
    "txt, step, expected_result",
    [
        ('abc', 3, 'xyz'),
        ('ABC', 3, 'XYZ'),
        ('abcde', 5, 'vwxyz'),
        ('ABCDE', 5, 'VWXYZ')
    ]
)
def test_decrypt_first_letters_abcde(txt, step, expected_result):
    cipher = Cipher()
    result = cipher.encrypt(txt, step)
    assert result == expected_result

def test_decrypt_when_step_equal_0():
    with pytest.raises(EnteredZeroStep):
        cipher = Cipher()
        cipher.decrypt('cat', 0)

def test_decrypt_when_step_is_negative():
    with pytest.raises(EnteredNegativeStep):
        cipher = Cipher()
        cipher.encrypt('cat', -3)

def test_decrypt_when_step_more_than_alphabet():
    with pytest.raises(EnteredStepMoreThanAlphabet):
        cipher = Cipher()
        cipher.encrypt('cat', 27)