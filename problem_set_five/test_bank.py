from bank import value

def test_word():
    assert value("Hello") == 0
    assert value("Bye") == 100
    assert value("Hey") == 20


