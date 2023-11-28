from src.cipher import Cipher, EnteredZeroStep, EnteredNegativeStep, EnteredStepMoreThanAlphabet
import pytest


@pytest.mark.parametrize(
    "txt, step, expected_result",
    [
        ('cat', 3, 'fdw'),
        ('cat', 5, 'hfy'),
        ('hello', 3, 'khoor'),
        ('hello', 5, 'mjqqt'),
    ]
)
def test_encrypt_lowercase(txt, step, expected_result):
    cipher = Cipher()
    result = cipher.encrypt(txt, step, True)
    assert result == expected_result


@pytest.mark.parametrize(
    "txt, step, expected_result",
    [
        ('Cat', 3, 'Fdw'),
        ('CAT', 5, 'HFY'),
        ('hellO', 3, 'khooR'),
        ('HELLO', 5, 'MJQQT')
    ]
)
def test_encrypt_uppercase(txt, step, expected_result):
    cipher = Cipher()
    result = cipher.encrypt(txt, step, True)
    assert result == expected_result


@pytest.mark.parametrize(
    "txt, step, expected_result",
    [
        ('123', 3, '456'),
        ('456', 3, '789')
    ]
)
def test_encrypt_digits(txt, step, expected_result):
    cipher = Cipher()
    result = cipher.encrypt(txt, step, True)
    assert result == expected_result


@pytest.mark.parametrize(
    "txt, step, expected_result",
    [
        ('xyz', 3, 'abc'),
        ('XYZ', 3, 'ABC'),
        ('vwxyz', 5, 'abcde'),
        ('VWXYZ', 5, 'ABCDE')
    ]
)
def test_encrypt_last_letters_xyz(txt, step, expected_result):
    cipher = Cipher()
    result = cipher.encrypt(txt, step, True)
    assert result == expected_result


def test_encrypt_limit_digits_for_value_9():
    txt = '9'
    step = 3
    expected_result = '2'
    cipher = Cipher()
    result = cipher.encrypt(txt, step, True)
    assert result == expected_result


def test_encrypt_when_step_equal_0():
    with pytest.raises(EnteredZeroStep):
        cipher = Cipher()
        cipher.encrypt('cat', 0, True)


def test_encrypt_when_step_is_negative():
    with pytest.raises(EnteredNegativeStep):
        cipher = Cipher()
        cipher.encrypt('cat', -3, True)


def test_encrypt_when_step_more_than_alphabet():
    with pytest.raises(EnteredStepMoreThanAlphabet):
        cipher = Cipher()
        cipher.encrypt('cat', 27, True)
