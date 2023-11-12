# -*- coding: utf-8 -*-
from pandas import NA
from pandas._libs.missing import NAType
from ... import ref_cadastrales as pyfunc_ref_cad
from ... import superficie as pyfunc_superficie


def short_id_from_parts(com_insee: str, section: str, numero: str, com_abs: str) -> NAType | str:
    try:
        return pyfunc_ref_cad.short_id_from_parts(com_insee, com_abs, section, numero)

    except:
        return NA


def idu_from_parts(com_insee: str, section: str, numero: str, com_abs: str = "000") -> NAType | str:
    try:
        return pyfunc_ref_cad.idu_from_parts(com_insee, com_abs, section, numero)

    except:
        return NA


def ref_parcelle_to_parts(ref: str) -> tuple[NAType | str, NAType | str, NAType | str, NAType | str]:
    try:
        return pyfunc_ref_cad.ref_parcelle_to_parts(ref)

    except:
        return NA, NA, NA, NA


def ref_parcelle_to_idu(ref: str) -> NAType | str:
    try:
        return pyfunc_ref_cad.ref_parcelle_to_idu(ref)

    except:
        return NA


def ref_parcelle_to_short_id(ref: str) -> NAType | str:
    try:
        return pyfunc_ref_cad.ref_parcelle_to_short_id(ref)

    except:
        return NA


def superficie_ha(sup_m2: float | int) -> NAType | float:
    try:
        return pyfunc_superficie.superficie_ha(sup_m2)

    except:
        return NA


def superficie_ha_a_ca(sup_m2: float | int) -> NAType | str:
    try:
        return pyfunc_superficie.superficie_ha_a_ca(sup_m2)

    except:
        return NA


def superficie_from_str(sup_string: str) -> NAType | int:
    try:
        return pyfunc_superficie.superficie_from_str(sup_string)

    except:
        return NA
