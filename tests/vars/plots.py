import pandas as pd
from pandas import NA


plot_1 = {'idu': '780480000H0011', 'superficie_ha': '17 ha 12 a 34 ca', 'superficie_m2': 171234}
plot_2 = {'idu': '780480000H0012', 'superficie_ha': '10 a 25 ca', 'superficie_m2': 1025.1}
plot_3 = {'idu': NA, 'superficie_ha': NA, 'superficie_m2': NA}
plot_4 = {'idu': None, 'superficie_ha': None, 'superficie_m2': None}

plots = [
    plot_1,
    plot_2,
]
df_plots = pd.DataFrame(plots)

plots_na_none = [
    plot_3,
    plot_4,
]
df_plots_na_none = pd.DataFrame(plots_na_none)

df_empty = pd.DataFrame()

df_only_one = pd.DataFrame([plot_1])

df_only_one_na = pd.DataFrame([plot_3])