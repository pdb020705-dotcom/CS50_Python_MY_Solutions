from fuel import convert

def test_greater_x():
    assert convert("8/6") == None

def test_zero_y():
    assert convert("1/0") == None

def test_str():
    assert convert("cat/dog") == None

def test_correct_input():
    assert convert("6/7") == "86%"