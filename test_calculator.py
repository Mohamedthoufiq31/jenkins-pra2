from calculator import add, subtract, multiply


def test_add():
    assert add(2, 4) == 6


def test_subtract():
    assert subtract(5, 1) == 4


def test_multiply():
    assert multiply(4, 3) == 12