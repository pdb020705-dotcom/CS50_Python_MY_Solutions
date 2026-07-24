from twttr import shorten
import pytest

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
     assert shorten("ISHOWSPEED") == "SHWSPD"
    
    
def test_number():
    assert shorten("50") == "50"

def test_punctuation():
    assert shorten(".hello") == ".hll"
