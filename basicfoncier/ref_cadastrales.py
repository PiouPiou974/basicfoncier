# -*- coding: utf-8 -*-
from .utils.string_manipulation import first_car_alpha


def idu_from_parts(com_insee: str, section: str, numero: str, com_abs: str = "000") -> str:
    """
    construis la référence cadastrale de la parcelle à partir de ses composants

    :param com_insee: code insee de la commune (ou de l'arrondissement) sur 5 caractères
    :param section: code de section sur 1 ou 2 caractères
    :param numero: numéro de la parcelle sur 1 à 4 caractères
    :param com_abs: code de commune absorbée pour les communes nouvelles
    :return: référence cadastrale de la parcelle au format idu (14 caractères)
    """

    return com_insee.zfill(5) + com_abs.zfill(3) + section.zfill(2) + numero.zfill(4)


def short_id_from_parts(com_insee: str, section: str, numero: str, com_abs: str = "") -> str:
    """
    construis le code identifiant court de la parcelle à partir de ses composants

    :param com_insee: code insee de la commune (ou de l'arrondissement) sur 5 caractères
    :param section: code de section sur 1 ou 2 caractères
    :param numero: numéro de la parcelle sur 1 à 4 caractères
    :param com_abs: code de commune absorbée pour les communes nouvelles
    :return: code identifiant court de la parcelle, maximum 14 caractères, minimum 7
    """

    if com_abs == "000":
        com_abs = ""

    return com_insee + com_abs + section.replace("0", "") + str(int(numero))


def ref_parcelle_to_parts(ref: str) -> tuple[str, str, str, str]:
    """
    Décompose une référence parcellaire en ses composants élémentaires. Gère les identifiants courts et
    les identifiants d'Alsace-Moselle seulement s'ils sont au format idu.

    :param ref: la référence à la parcelle
    :return: Code insee commune, code de commune absorbée, code de section, numéro parcellaire
    """

    # Alsace-Moselle : code uniquement numérique.
    if ref.startswith('57') or ref.startswith('67') or ref.startswith('68'):
        assert len(ref) == 14
        assert ref.isnumeric()
        return ref[0:5], ref[8:10], ref[10:], ref[5:8]

    assert 7 <= len(ref) <= 14
    com_insee = ref[0:5]

    # si les 3 prochains caractères existent et sont numériques, alors c'est un code de commune absorbée
    if len(ref) >= 8:
        if ref[5:8].isnumeric():
            com_abs = ref[5:8]
        else:
            com_abs = None
    else:
        com_abs = None
    # on calcule la chaîne de caractère restante, contenant normalement un code section avec un caractère
    # alphanumérique et un code parcelle.
    ref_restante = ref[5 if com_abs is None else 8:]
    com_abs = com_abs or '000'

    assert len(ref_restante) >= 2
    # On trouve le dernier caractère alphanumérique
    last_alpha = len(ref_restante) - first_car_alpha(ref_restante[::-1])
    assert last_alpha != -1
    assert last_alpha <= 2
    section = ref_restante[:last_alpha]
    numero = ref_restante[last_alpha:]
    assert numero != ''
    return com_insee.zfill(5), section.zfill(2), numero.zfill(4), com_abs.zfill(3)


def ref_parcelle_to_idu(ref: str) -> str:
    """
    Calcule l'idu d'une parcelle à partir d'une référence cadastrale plus courte

    :param ref: une référence cadastrale
    :return: idu (14 caractères)
    """
    com_insee, section, numero, com_abs = ref_parcelle_to_parts(ref)
    return idu_from_parts(com_insee, section, numero, com_abs)


def ref_parcelle_to_short_id(ref: str) -> str:
    """
    Calcule l'id court d'une parcelle à partir d'une référence cadastrale

    :param ref: une référence cadastrale
    :return: id (7 à 14 caractères)
    """
    com_insee, section, numero, com_abs = ref_parcelle_to_parts(ref)
    return short_id_from_parts(com_insee, section, numero, com_abs)
