"""
Tests unitaires de la fonction addition().
"""

from fonctions import addition


def test_addition_positive():
    """
    Vérifie l'addition de deux nombres positifs.
    """
    assert addition(2, 3) == 5


def test_addition_negative():
    """
    Vérifie l'addition de deux nombres négatifs.
    """
    assert addition(-2, -3) == -5