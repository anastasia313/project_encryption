from project_encryption.src.cipher import Cipher, EnteredZeroStep, EnteredNegativeStep, EnteredStepMoreThanAlphabet, ProvidedEmptyData
import pytest
import os

THIS_DIR = os.path.dirname(__file__)


@pytest.mark.parametrize(
    'expected_path',
    (os.path.join(THIS_DIR, 'json_files/example.json'),),
)
def test_encrypt_json(expected_path):
    expected_result = {"data": [
            {"cipher": "bcde"},
            {"cipher": "bcde"},
            {"cipher": "bcde"}
            ]
    }
    cipher = Cipher()
    result = cipher.encrypt_json(expected_path, True)
    assert result == expected_result


@pytest.mark.parametrize(
    'expected_path',
    (os.path.join(THIS_DIR, 'json_files/empty.json'),),
)
def test_encrypt_json_when_file_is_empty(expected_path):
    with pytest.raises(ProvidedEmptyData):
        cipher = Cipher()
        cipher.encrypt_json(expected_path, True)



@pytest.mark.parametrize(
    'expected_path',
    (os.path.join(THIS_DIR, 'json_files/zero.json'),),
)
def test_encrypt_json_when_step_is_0(expected_path):
    with pytest.raises(EnteredZeroStep):
        cipher = Cipher()
        cipher.encrypt_json(expected_path, True)


@pytest.mark.parametrize(
    'expected_path',
    (os.path.join(THIS_DIR, 'json_files/negative.json'),),
)
def test_encrypt_when_step_is_negative(expected_path):
    with pytest.raises(EnteredNegativeStep):
        cipher = Cipher()
        cipher.encrypt_json(expected_path,True)


@pytest.mark.parametrize(
    'expected_path',
    (os.path.join(THIS_DIR, 'json_files/out_of_range.json'),),
)
def test_encrypt_when_step_more_than_alphabet(expected_path):
    with pytest.raises(EnteredStepMoreThanAlphabet):
        cipher = Cipher()
        cipher.encrypt_json(expected_path,True)




