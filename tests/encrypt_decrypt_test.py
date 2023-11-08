from functionality.cipher_implementation import Cipher
import pytest


@pytest.mark.parametrize(
    "txt, expected_result",
    [
        ('ada', 'dgd'),
        ('DFD', 'GIG'),
        ('df3fd.', 'gi6ig.'),
        ('DFR#D+sd3', 'GIU#G+vg6')
    ]
)

def test_encrypt(txt, expected_result):
    cipher = Cipher()
    result = cipher.encrypt(txt)
    assert result == expected_result

@pytest.mark.parametrize(
    "txt, expected_result",
    [
        ('klk', 'hih'),
        ('FRF', 'COC'),
        ('.bhnkrt', '.yekhoq'),
        ('F>H,HT+dh', 'C>E,EQ+ae')
    ]
)

def test_decrypt(txt, expected_result):
    cipher = Cipher()
    result = cipher.decrypt(txt)
    assert result == expected_result


def test_encrypt_json():
    file = "C:/Users/nasta/python_encrypto/functionality/keys.json"
    expected_result = {1: 'dg56dgd',
                       2: 'vgvg',
                       3: 'yvnkvinj',
                       4: 'jjomu76voj',
                       5: 'ygyggy',
                       6: 'vvgdvg',
                       7: 'yyyyg.9gi',
                       8: 'tzhuwb'}
    cipher = Cipher()
    result = cipher.encrypt_json(file)
    assert result == expected_result

def test_decrypt_json():
    file = "C:/Users/nasta/python_encrypto/functionality/keys.json"
    expected_result = {1: 'xa90xax',
                       2: 'papa',
                       3: 'sphepchd',
                       4: 'ddigo10pid',
                       5: 'sasaas',
                       6: 'ppaxpa',
                       7: 'ssssa.3ac',
                       8: 'ntboqv'}
    cipher = Cipher()
    result = cipher.decrypt_json(file)
    assert result == expected_result




