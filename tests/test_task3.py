from tasks.task3 import factorial

def test_factorial_basic():
    assert factorial(5) == 120

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_negative():
    assert factorial(-3) is None
