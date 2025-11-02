from tasks.task2 import is_palindrome

def test_palindrome_true():
    assert is_palindrome("kajak")
    assert is_palindrome("Anna".lower())

def test_palindrome_false():
    assert not is_palindrome("python2")
