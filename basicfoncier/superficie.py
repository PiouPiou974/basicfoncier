# -*- coding: utf-8 -*-


def superficie_ha(sup_m2: float | int) -> float:
    """
    Renvoie une superficie en hectare
    :param sup_m2: la superficie en m²
    :return: la superficie en ha (float)
    """
    return sup_m2 / 10000


def superficie_ha_a_ca(sup_m2: float | int) -> str:
    """
    Renvoie la superficie formatée en "_ ha __ a __ ca"
    :param sup_m2: la superficie en m²
    :return: str
    """
    _ha = int(sup_m2 / 10000)
    _a = int(sup_m2 / 100) - 100 * _ha
    _ca = int(sup_m2) - 100 * _a - 10000 * _ha
    if _ha != 0:
        return f'{_ha} ha {_a: 2} a {_ca: 2} ca'
    if _a != 0:
        return f'{_a} a {_ca} ca'
    return f'{_ca} ca'


def superficie_from_str(sup_string: str) -> int:
    """
    Récupère la valeur en m² depuis une superficie formatée en "_ ha __ a __ ca"
    :param sup_string: chaîne de caractères
    :return: int
    """
    return int(sup_string.replace(" ", "").replace("a", "").replace("c", "").replace("h", ""))
