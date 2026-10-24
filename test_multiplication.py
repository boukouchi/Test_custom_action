"""
Tests unitaires de la fonction multiplication().
"""

from fonctions import multiplication


def test_multiplication_positive():
    """
    Vérifie la multiplication de deux nombres positifs.
    """
    assert multiplication(4, 3) == 12


def test_multiplication_par_zero():
    """
    Vérifie la multiplication par zéro.
    """
    assert multiplication(4, 0) == 0