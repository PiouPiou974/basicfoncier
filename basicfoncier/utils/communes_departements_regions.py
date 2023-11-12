# -*- coding: utf-8 -*-


def code_dep_from_com_insee(com_insee: str) -> str:
    """
    Renvoie le code département sur 2 ou 3 caractères d'après le code Insee de la commune
    :param com_insee: le code insee de la commune sur 5 caractères
    :return:
    """
    assert len(com_insee) == 5
    if com_insee.startswith("97") or com_insee.startswith("98"):
        return com_insee[0:3]
    else:
        return com_insee[0:2]


def code_com_from_com_insee(com_insee: str) -> str:
    """
    Renvoie le code commune sur 2 ou 3 caractères d'après le code Insee de la commune
    :param com_insee: le code insee de la commune sur 5 caractères
    :return:
    """
    assert len(com_insee) == 5
    if com_insee.startswith("97") or com_insee.startswith("98"):
        return com_insee[3:5]
    else:
        return com_insee[2:5]


def com_insee_from_code_dep_code_com(code_dep: str, code_com: str) -> str:
    """
    Renvoie le code insee d'une commune d'après les codes département et commune
    :param code_dep: le code département sur 2 ou 3 chiffres (outre-mer)
    :param code_com: le code commune sur 3 ou 2 chiffres (outre-mer)
    :return: dode insee commune sur 5 chiffres
    """
    if len(code_dep) == 3:
        code_dep = code_dep[:2]

    return code_dep + code_com


def com_insee_com_arrdt_from_insee(code_insee: str) -> tuple[str, str]:
    """
    Calcule le code d'arrondissement et le code insee général de la commune à partir du code insee d'un arondissement.
    Exemple : com_insee_com_arrdt_from_insee("75104") -> ("75100", "104")
    :param code_insee: le code insee sur 5 chiffre de l'arrondissement
    :return: le code insee commune et le code de l'arrondissement sur 3 chiffres
    """

    arrondissements_paris = {
        "75101",
        "75102",
        "75103",
        "75104",
        "75105",
        "75106",
        "75107",
        "75108",
        "75109",
        "75110",
        "75111",
        "75112",
        "75113",
        "75114",
        "75115",
        "75116",
        "75117",
        "75118",
        "75119",
        "75120"
    }
    arrondissements_lyon = {
        "69381",
        "69382",
        "69383",
        "69384",
        "69385",
        "69386",
        "69387",
        "69388",
        "69389"
    }
    arrondissements_marseille = {
        "13201",
        "13202",
        "13203",
        "13204",
        "13205",
        "13206",
        "13207",
        "13208",
        "13209",
        "13210",
        "13211",
        "13212",
        "13213",
        "13214",
        "13215",
        "13216"
    }

    if code_insee in arrondissements_paris:
        return "75100", code_insee[2:]

    if code_insee in arrondissements_lyon:
        return "69300", code_insee[2:]

    if code_insee in arrondissements_marseille:
        return "13055", code_insee[2:]

    return code_insee, "000"

