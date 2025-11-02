"""
Zadanie 2: Napisz funkcję is_palindrome(s), która zwraca True jeśli napis s jest palindromem.
"""

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
