"""Tests for data processing"""
from unit_testing.phonebook_pytest.phonebook.data_processing import clean_phonenumber


def test_clean_phonenumber():
    assert "0392987230" == clean_phonenumber("039 298-72-30")
