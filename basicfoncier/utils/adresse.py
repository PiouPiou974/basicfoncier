# -*- coding: utf-8 -*-


def adresse(numero="", voie: str = ""):
    numero = str(numero)
    if voie != "":
        voie = " " + voie
    return numero + voie
