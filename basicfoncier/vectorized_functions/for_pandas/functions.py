# -*- coding: utf-8 -*-
import numpy as np
from . import _nullable


short_id_from_parts = np.vectorize(_nullable.short_id_from_parts)
idu_from_parts = np.vectorize(_nullable.idu_from_parts)
ref_parcelle_to_parts = np.vectorize(_nullable.ref_parcelle_to_parts)
ref_parcelle_to_idu = np.vectorize(_nullable.ref_parcelle_to_idu)
ref_parcelle_to_short_id = np.vectorize(_nullable.ref_parcelle_to_short_id)
superficie_ha = np.vectorize(_nullable.superficie_ha)
superficie_ha_a_ca = np.vectorize(_nullable.superficie_ha_a_ca)
superficie_from_str = np.vectorize(_nullable.superficie_from_str)
