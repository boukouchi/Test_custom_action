"""
Programme principal.
"""

from fonctions import addition, multiplication


def main():
    """
    Fonction principale du programme.
    """
    nombre1 = 10
    nombre2 = 5

    print(f"Addition : {addition(nombre1, nombre2)}")
    print(f"Multiplication : {multiplication(nombre1, nombre2)}")


if __name__ == "__main__":
    main()