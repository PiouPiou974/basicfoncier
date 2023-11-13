# -*- coding: utf-8 -*-
import numpy as np
from . import _nullable


short_id_from_parts = np.vectorize(_nullable.short_id_from_parts, otypes='O')
idu_from_parts = np.vectorize(_nullable.idu_from_parts, otypes='O')
ref_parcelle_to_parts = np.vectorize(_nullable.ref_parcelle_to_parts, otypes=['O', 'O', 'O', 'O'])
ref_parcelle_to_idu = np.vectorize(_nullable.ref_parcelle_to_idu, otypes='O')
ref_parcelle_to_short_id = np.vectorize(_nullable.ref_parcelle_to_short_id, otypes='O')
superficie_ha = np.vectorize(_nullable.superficie_ha, otypes='O')
superficie_ha_a_ca = np.vectorize(_nullable.superficie_ha_a_ca, otypes='O')
superficie_from_str = np.vectorize(_nullable.superficie_from_str, otypes='O')
