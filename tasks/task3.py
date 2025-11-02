"""
Zadanie 3: Napisz funkcję factorial(n), która zwraca silnię liczby n.
Dla n < 0 zwróć None.
"""


def factorial(n):
    if (n < 0):
        return None
    if (n == 0 or n == 1):
        return 1
    return factorial(n - 1) * n
