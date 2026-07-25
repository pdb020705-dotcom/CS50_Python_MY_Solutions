from plates import is_valid
import pytest

def test_str():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_int():
    with pytest.raises(TypeError):
        is_valid(50)