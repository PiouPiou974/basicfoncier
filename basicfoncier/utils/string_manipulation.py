# -*- coding: utf-8 -*-


def first_car_alpha(s: str) -> int:
    """
    Renvoie le premier caractère alphabétique d'une chaîne de caractères, -1 sinon.
    :param s: chaîne de caractères
    :return: int
    """
    try:
        return [x.isalpha() for x in s].index(True)
    except ValueError:
        return -1


def first_car_numeric(s: str) -> int:
    """
        Renvoie le premier caractère numérique d'une chaîne de caractères, -1 sinon.
        :param s: chaîne de caractères
        :return: int
        """
    try:
        return [x.isnumeric() for x in s].index(True)
    except ValueError:
        return -1
