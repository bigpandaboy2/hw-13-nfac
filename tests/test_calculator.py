from poetry_test_project.calculator import add_numbers

def test_add_numbers_positive():
    assert add_numbers(1, 2) == 3
    assert add_numbers(5, 3) == 8

def test_add_numbers_negative():
    assert add_numbers(-1, -2) == -3
    assert add_numbers(-5, 5) == 0

def test_add_numbers_zero():
    assert add_numbers(0, 0) == 0
    assert add_numbers(1, 0) == 1