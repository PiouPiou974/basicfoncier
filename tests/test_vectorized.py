from basicfoncier.vectorized_functions.for_pandas.functions import ref_parcelle_to_parts, superficie_from_str, superficie_ha_a_ca
from pandas import NA
from vars.plots import df_plots, df_plots_na_none, df_only_one_na, df_only_one, df_empty
from numpy import array

arr = array(['1 ha  13 a  20 ca', '1 ha  0 a  3 ca', '22 a 97 ca',
       '1 ha  4 a  70 ca', '59 a 95 ca', '14 a 93 ca', '42 a 89 ca',
       '26 a 60 ca', '3 a 30 ca', '10 a 18 ca', '65 ca', '4 a 10 ca',
       '1 a 50 ca', '2 a 10 ca', '11 a 90 ca', '6 a 90 ca', '14 a 24 ca',
       '2 a 96 ca', '75 ca', '1 a 60 ca', '27 ca', '2 a 15 ca',
       '3 a 50 ca', '13 a 50 ca', '1 a 0 ca', '1 a 25 ca', '88 ca',
       '1 a 0 ca', '1 a 0 ca', '1 a 58 ca', '1 a 35 ca', '65 ca', '75 ca',
       '1 a 50 ca', '95 ca', '1 a 55 ca', '1 a 5 ca', '1 a 40 ca',
       '2 a 15 ca', '18 a 95 ca', '58 ca', '44 ca', '60 ca', '4 a 95 ca',
       '30 ca', '2 a 0 ca', '1 a 5 ca', '1 a 20 ca', '1 a 30 ca',
       '1 a 15 ca', '1 a 55 ca', '7 a 10 ca', '6 a 0 ca', '5 a 40 ca',
       '1 a 14 ca', '61 ca', '1 a 10 ca', '60 ca', '18 a 60 ca',
       '2 a 98 ca', '85 ca', '2 a 40 ca', '33 ca', '6 a 68 ca',
       '1 a 95 ca', '1 a 10 ca', '89 ca', '2 a 68 ca', '1 a 81 ca',
       '1 a 52 ca', '1 a 50 ca', '2 a 41 ca', '2 a 26 ca', '1 a 30 ca',
       '2 a 49 ca', '2 a 63 ca', '3 a 45 ca', '3 a 68 ca', '3 a 58 ca',
       '4 a 34 ca', '2 a 41 ca', '1 a 80 ca', '7 ca', '13 ca',
       '1 a 30 ca', '5 ca', '1 a 64 ca', '16 ca', '1 a 74 ca',
       '3 a 85 ca', '4 a 90 ca', '4 a 29 ca', '4 a 59 ca', '4 a 71 ca',
       '4 a 25 ca', '3 a 97 ca', '4 a 3 ca', '4 a 8 ca', '4 a 50 ca',
       '4 a 69 ca', '4 a 62 ca', '2 a 16 ca', '2 a 16 ca', '2 a 16 ca',
       '2 a 16 ca', '2 a 16 ca', '2 a 34 ca', '2 a 34 ca', '2 a 34 ca',
       '2 a 17 ca', '2 a 33 ca', '2 a 43 ca', '2 a 38 ca', '4 a 31 ca',
       '2 a 16 ca', '2 a 34 ca', '2 a 16 ca', '3 a 23 ca', '2 a 49 ca',
       '2 a 43 ca', '2 a 86 ca', '2 a 80 ca', '10 a 10 ca', '11 a 45 ca',
       '2 a 65 ca', '3 a 50 ca', '90 ca', '95 ca', '68 ca', '85 ca',
       '96 ca', '1 a 55 ca', '2 a 10 ca', '95 ca', '2 a 55 ca',
       '2 a 55 ca', '1 a 25 ca', '20 ca', '1 a 38 ca', '12 ca', '45 ca',
       '1 a 30 ca', '77 ca', '1 a 50 ca', '75 ca', '35 ca', '83 ca',
       '2 a 75 ca', '1 a 85 ca', '82 ca', '1 a 65 ca', '55 ca', '12 ca',
       '10 ca', '1 a 7 ca', '4 a 55 ca', '4 ca', '10 ca', '2 ca',
       '1 a 96 ca', '1 a 67 ca', '1 a 15 ca', '1 a 30 ca', '3 a 90 ca',
       '1 a 10 ca', '45 ca', '1 a 50 ca', '60 ca', '1 a 65 ca', '55 ca',
       '70 ca', '34 ca', '1 a 47 ca', '19 ca', '88 ca', '2 a 85 ca',
       '9 ca', '8 ca', '4 ca', '59 ca', '8 ca', '63 ca', '28 ca', '61 ca',
       '33 ca', '1 a 78 ca', '1 a 31 ca', '1 a 48 ca', '49 ca', '81 ca',
       '6 a 0 ca', '2 a 30 ca', '1 a 25 ca', '59 ca', '3 a 10 ca',
       '57 ca', '2 a 38 ca', '15 ca', '1 a 25 ca', '1 a 35 ca',
       '1 a 10 ca', '1 a 46 ca', '2 a 0 ca', '5 a 25 ca', '85 ca',
       '1 a 40 ca', '<NA>', '93 ca', '1 a 80 ca', '80 ca', '1 a 60 ca',
       '1 a 60 ca', '3 a 65 ca', '3 a 35 ca', '3 a 75 ca', '21 ca',
       '7 ca', '1 a 25 ca', '2 a 30 ca', '8 ca', '2 a 29 ca', '31 ca',
       '4 a 25 ca', '1 a 16 ca', '1 a 17 ca', '1 a 25 ca', '3 ca',
       '1 a 47 ca', '39 ca', '24 ca', '96 ca', '1 a 15 ca', '1 a 5 ca',
       '1 a 30 ca', '1 a 20 ca', '1 a 50 ca', '1 a 41 ca', '1 a 55 ca',
       '2 a 95 ca', '8 ca', '3 a 2 ca', '1 a 65 ca', '2 a 15 ca', '65 ca',
       '1 a 45 ca', '1 a 40 ca', '20 ca', '10 ca', '29 ca', '1 a 35 ca',
       '65 ca', '2 a 90 ca', '1 a 10 ca', '3 a 80 ca', '70 ca', '70 ca',
       '1 a 0 ca', '1 a 27 ca', '3 a 95 ca', '1 a 36 ca', '1 a 0 ca',
       '13 ca', '60 ca', '82 ca', '13 ca', '13 ca', '11 ca', '1 a 30 ca',
       '1 a 10 ca', '15 ca', '1 a 13 ca', '23 ca', '10 ca', '92 ca',
       '37 ca', '1 a 88 ca', '2 a 17 ca', '67 ca', '1 a 59 ca', '17 ca',
       '3 ca', '3 a 5 ca', '1 a 37 ca', '1 a 32 ca', '69 ca', '1 a 96 ca',
       '2 a 2 ca', '2 a 40 ca', '3 a 10 ca', '2 a 34 ca', '2 a 35 ca',
       '2 a 36 ca', '2 a 13 ca', '2 a 13 ca', '2 a 33 ca', '2 a 62 ca',
       '3 ca', '24 ca', '2 a 75 ca', '1 a 60 ca', '26 ca', '57 ca',
       '2 a 13 ca', '2 a 5 ca', '53 ca', '2 a 56 ca', '2 a 64 ca',
       '2 a 80 ca', '3 a 5 ca', '3 a 45 ca', '1 a 10 ca', '23 ca',
       '1 a 30 ca', '68 ca', '2 a 25 ca', '2 a 92 ca', '1 a 0 ca',
       '1 a 10 ca', '1 a 85 ca', '3 a 80 ca', '2 a 0 ca', '2 a 12 ca',
       '1 a 58 ca', '2 a 25 ca', '8 ca', '1 a 33 ca', '13 ca', '52 ca',
       '2 a 9 ca', '3 a 11 ca', '2 a 31 ca', '41 ca', '3 a 72 ca',
       '45 ca', '67 ca', '75 ca', '1 a 61 ca', '2 a 17 ca', '1 a 43 ca',
       '15 ca', '2 a 44 ca', '2 a 46 ca', '90 ca', '17 ca', '34 ca',
       '2 a 28 ca', '1 a 70 ca', '95 ca', '8 ca', '30 ca', '1 a 40 ca',
       '1 a 0 ca', '1 a 55 ca', '7 ca', '15 ca', '2 a 13 ca', '12 ca',
       '2 a 20 ca', '2 a 30 ca', '2 a 30 ca', '72 ca', '2 a 48 ca',
       '3 a 17 ca', '83 ca', '2 a 30 ca', '2 a 65 ca', '2 a 95 ca',
       '2 a 90 ca', '1 a 16 ca', '2 a 25 ca', '2 a 5 ca', '19 ca', '8 ca',
       '1 a 27 ca', '1 a 96 ca', '14 ca', '1 a 6 ca', '2 a 15 ca',
       '2 a 75 ca', '2 a 25 ca', '10 ca', '74 ca', '2 a 98 ca',
       '8 a 77 ca', '8 ca', '1 a 69 ca', '61 ca', '1 a 96 ca', '7 ca',
       '1 a 5 ca', '89 ca', '49 ca', '1 a 5 ca', '63 ca', '36 ca',
       '10 ca', '9 ca', '13 ca', '1 a 24 ca', '14 ca', '14 ca', '61 ca',
       '48 ca', '41 ca', '2 a 91 ca', '1 a 4 ca', '95 ca', '95 ca',
       '1 a 5 ca', '85 ca', '45 ca', '70 ca', '80 ca', '2 a 45 ca',
       '70 ca', '1 a 75 ca', '83 ca', '1 a 38 ca', '12 ca', '2 a 0 ca',
       '1 a 10 ca', '65 ca', '93 a 0 ca', '11 ha  80 a  90 ca',
       '1 ha  62 a  65 ca', '39 a 25 ca', '6 ha  96 a  10 ca',
       '1 ha  60 a  64 ca', '9 ha  68 a  75 ca', '3 ha  91 a  35 ca',
       '1 ha  6 a  20 ca', '3 ha  4 a  15 ca', '43 a 80 ca',
       '2 ha  83 a  85 ca', '1 ha  9 a  65 ca', '56 a 95 ca',
       '55 a 53 ca', '60 a 37 ca', '1 ha  14 a  15 ca',
       '1 ha  6 a  21 ca', '60 a 75 ca', '31 a 77 ca', '60 a 70 ca',
       '1 ha  17 a  80 ca', '41 a 46 ca', '25 a 35 ca', '4 a 15 ca',
       '6 a 50 ca', '12 a 52 ca', '12 a 50 ca', '4 a 72 ca', '4 a 25 ca',
       '4 a 48 ca', '4 a 88 ca', '6 a 70 ca', '7 a 50 ca', '95 ca',
       '26 a 95 ca', '3 a 0 ca', '17 a 40 ca', '2 a 70 ca', '22 a 34 ca',
       '151 ha  68 a  10 ca', '60 ha  1 a  85 ca', '66 ha  5 a  60 ca',
       '90 ha  57 a  23 ca', '90 ha  63 a  70 ca', '71 ha  73 a  75 ca',
       '39 ha  37 a  60 ca', '10 ha  82 a  53 ca', '9 ha  13 a  38 ca',
       '23 ha  56 a  50 ca', '26 ha  58 a  85 ca', '31 ha  60 a  20 ca',
       '9 ha  67 a  53 ca', '24 ha  95 a  25 ca', '1 ha  77 a  50 ca',
       '15 ha  42 a  55 ca', '15 ha  10 a  32 ca', '12 ha  73 a  43 ca',
       '11 ha  19 a  25 ca', '7 ha  47 a  50 ca', '17 ha  54 a  10 ca',
       '2 ha  84 a  0 ca', '69 a 0 ca', '7 ha  94 a  0 ca',
       '3 ha  0 a  25 ca', '1 ha  15 a  50 ca', '1 ha  86 a  0 ca',
       '1 ha  75 a  40 ca', '3 ha  16 a  75 ca', '1 ha  19 a  43 ca',
       '73 a 75 ca', '1 ha  84 a  11 ca', '92 a 19 ca',
       '1 ha  13 a  66 ca', '1 ha  3 a  7 ca', '1 ha  43 a  78 ca',
       '1 ha  38 a  99 ca', '86 a 20 ca', '67 a 0 ca',
       '1 ha  58 a  75 ca', '32 a 55 ca', '69 a 63 ca', '88 a 75 ca',
       '83 a 80 ca', '60 a 5 ca', '94 a 77 ca', '30 a 0 ca', '34 a 24 ca',
       '65 a 0 ca', '78 a 68 ca', '26 a 32 ca', '37 a 50 ca',
       '22 a 75 ca', '11 a 27 ca', '15 a 51 ca', '33 a 72 ca',
       '15 a 97 ca', '14 a 52 ca', '42 a 23 ca', '40 a 53 ca',
       '49 a 90 ca', '32 a 16 ca', '35 a 44 ca', '13 a 75 ca',
       '20 a 0 ca', '7 a 29 ca', '25 a 0 ca', '19 a 75 ca', '8 a 20 ca',
       '12 a 0 ca', '11 a 50 ca', '8 a 80 ca', '28 a 49 ca', '10 a 17 ca',
       '3 a 5 ca', '4 a 28 ca', '6 a 17 ca', '7 a 20 ca', '4 a 76 ca',
       '2 a 55 ca', '2 a 29 ca', '2 a 7 ca', '5 a 48 ca', '5 a 62 ca',
       '5 a 50 ca', '4 a 72 ca', '5 a 21 ca', '5 a 21 ca', '19 a 88 ca',
       '4 a 47 ca', '5 a 20 ca', '5 a 19 ca', '5 a 18 ca', '5 a 18 ca',
       '5 a 21 ca', '5 a 35 ca', '5 a 20 ca', '5 a 19 ca', '5 a 19 ca',
       '5 a 18 ca', '5 a 17 ca', '5 a 17 ca', '5 a 16 ca', '19 a 11 ca',
       '2 a 14 ca', '1 a 63 ca', '1 a 64 ca', '1 a 65 ca', '1 a 67 ca',
       '1 a 67 ca', '1 a 68 ca', '1 a 68 ca', '1 a 69 ca', '5 a 47 ca',
       '1 a 69 ca', '2 a 22 ca', '1 a 65 ca', '1 a 68 ca', '1 a 69 ca',
       '1 a 70 ca', '1 a 69 ca', '1 a 70 ca', '1 a 70 ca', '6 a 63 ca',
       '4 a 34 ca', '11 a 32 ca', '3 a 91 ca', '2 a 28 ca', '3 a 34 ca',
       '5 a 13 ca', '3 a 57 ca', '2 a 62 ca', '3 a 61 ca', '3 a 58 ca',
       '3 a 37 ca', '1 a 83 ca', '1 a 87 ca', '2 a 43 ca', '2 a 97 ca',
       '2 a 40 ca', '1 a 60 ca', '12 a 50 ca', '2 a 39 ca', '8 a 40 ca',
       '2 a 88 ca', '3 a 39 ca', '5 a 84 ca', '2 a 9 ca', '4 a 84 ca',
       '5 a 0 ca', '14 a 92 ca', '2 a 41 ca', '3 a 32 ca', '2 a 43 ca',
       '2 a 96 ca', '2 a 20 ca', '2 a 5 ca', '1 a 88 ca', '1 a 82 ca',
       '79 ca', '37 ca', '94 ca', '19 ca', '54 ca', '95 ca', '1 a 48 ca',
       '2 a 1 ca', '2 a 8 ca', '1 a 62 ca', '1 a 35 ca', '2 a 0 ca',
       '1 a 90 ca', '1 a 37 ca', '83 ca', '82 ca', '2 a 9 ca',
       '2 a 40 ca', '2 a 27 ca', '2 a 19 ca', '2 a 24 ca', '1 a 92 ca',
       '2 a 5 ca', '2 a 12 ca', '2 a 14 ca', '2 a 1 ca', '1 a 91 ca',
       '1 a 90 ca', '2 a 14 ca', '1 a 43 ca', '85 ca', '22 ca', '83 ca',
       '1 a 35 ca', '96 ca', '26 ca', '1 a 28 ca', '8 ca', '2 a 17 ca',
       '2 a 3 ca', '1 a 76 ca', '71 ca', '4 ca', '2 a 50 ca',
       '27 a 75 ca', '87 ca', '1 a 98 ca', '1 a 54 ca', '1 a 82 ca',
       '2 a 47 ca', '2 a 75 ca', '6 a 65 ca', '1 a 78 ca', '3 a 1 ca',
       '3 ca', '2 a 24 ca', '8 a 23 ca', '4 a 34 ca', '1 a 36 ca',
       '4 a 17 ca', '13 ha  59 a  4 ca', '3 ha  96 a  95 ca',
       '5 ha  75 a  30 ca', '11 ha  26 a  34 ca', '3 ha  44 a  95 ca',
       '45 a 7 ca', '5 ha  62 a  70 ca', '42 a 41 ca', '93 a 2 ca',
       '98 a 80 ca', '1 ha  50 a  60 ca', '17 a 22 ca',
       '1 ha  49 a  60 ca', '18 a 50 ca', '39 a 0 ca', '1 ha  1 a  99 ca',
       '19 a 57 ca', '41 a 55 ca', '26 a 55 ca', '28 a 64 ca',
       '52 a 10 ca', '53 a 27 ca', '21 a 38 ca', '27 a 38 ca',
       '29 a 78 ca', '39 a 20 ca', '20 a 54 ca', '25 a 40 ca',
       '43 a 85 ca', '19 a 22 ca', '17 a 77 ca', '52 a 87 ca',
       '12 a 65 ca', '11 a 5 ca', '23 a 60 ca', '12 a 10 ca',
       '13 a 85 ca', '11 a 85 ca', '14 a 55 ca', '14 a 78 ca',
       '6 a 48 ca', '7 a 64 ca', '5 a 84 ca', '3 a 40 ca', '5 a 38 ca',
       '7 a 20 ca', '9 a 23 ca', '6 a 82 ca', '5 a 22 ca', '6 a 10 ca',
       '21 a 79 ca', '19 a 87 ca', '11 a 56 ca', '23 a 55 ca',
       '4 a 37 ca', '6 a 9 ca', '7 a 18 ca', '6 a 13 ca', '12 a 98 ca',
       '20 a 99 ca', '3 a 80 ca', '1 a 64 ca', '8 a 18 ca', '70 ca',
       '1 a 11 ca', '13 a 27 ca', '27 a 15 ca', '30 a 0 ca', '19 a 15 ca',
       '9 a 96 ca', '5 a 50 ca', '3 a 8 ca', '4 a 30 ca', '5 a 96 ca',
       '7 a 60 ca', '21 a 22 ca', '34 a 65 ca', '3 a 90 ca', '1 a 73 ca',
       '2 a 18 ca', '19 a 75 ca', '13 a 27 ca', '19 a 84 ca',
       '20 a 32 ca', '4 a 0 ca', '15 a 70 ca', '7 a 29 ca', '7 a 50 ca',
       '13 a 56 ca', '15 a 42 ca', '6 a 12 ca', '14 a 42 ca', '5 a 10 ca',
       '35 a 50 ca', '11 a 65 ca', '13 a 25 ca', '4 a 37 ca', '17 a 5 ca',
       '7 a 10 ca', '13 a 65 ca', '7 a 70 ca', '8 a 98 ca', '15 a 65 ca',
       '5 a 35 ca', '23 a 55 ca', '9 a 45 ca', '1 a 65 ca', '3 a 70 ca',
       '6 a 40 ca', '2 a 12 ca', '10 a 65 ca', '6 a 30 ca', '8 a 40 ca',
       '11 a 13 ca', '4 a 65 ca', '3 a 55 ca', '6 a 35 ca', '5 a 20 ca',
       '4 a 15 ca', '8 a 85 ca', '2 a 75 ca', '1 a 75 ca', '28 a 1 ca',
       '7 a 82 ca', '4 a 18 ca', '14 a 2 ca', '27 a 10 ca', '10 a 35 ca',
       '14 a 55 ca', '15 a 30 ca', '1 a 90 ca', '8 a 92 ca', '50 ca',
       '18 ha  53 a  37 ca', '67 ha  16 a  85 ca', '83 ha  72 a  50 ca',
       '36 ha  99 a  35 ca', '15 ha  12 a  23 ca', '101 ha  82 a  50 ca',
       '93 ha  48 a  10 ca', '31 ha  67 a  10 ca', '29 ha  48 a  50 ca',
       '5 ha  53 a  10 ca', '13 ha  50 a  10 ca', '61 ha  76 a  85 ca',
       '26 ha  58 a  70 ca', '11 ha  40 a  50 ca', '4 ha  81 a  0 ca',
       '9 ha  34 a  50 ca', '5 ha  70 a  10 ca', '5 ha  22 a  0 ca',
       '5 ha  53 a  25 ca', '5 ha  64 a  75 ca', '6 ha  75 a  0 ca',
       '4 ha  97 a  54 ca', '2 ha  44 a  50 ca', '33 a 0 ca',
       '3 ha  11 a  0 ca', '1 ha  41 a  75 ca', '72 a 75 ca', '81 a 0 ca',
       '75 a 85 ca', '56 a 0 ca', '95 a 55 ca', '1 ha  0 a  5 ca',
       '41 a 75 ca', '41 a 45 ca', '49 a 20 ca', '63 a 80 ca',
       '57 a 35 ca', '1 ha  98 a  75 ca', '4 ha  72 a  71 ca',
       '2 ha  84 a  25 ca', '2 ha  5 a  0 ca', '1 ha  63 a  50 ca',
       '2 ha  11 a  75 ca', '1 ha  40 a  0 ca', '75 a 25 ca', '20 a 0 ca',
       '42 a 90 ca', '42 a 20 ca', '51 a 72 ca', '81 a 45 ca',
       '11 a 65 ca', '13 a 45 ca', '20 a 0 ca', '17 a 85 ca',
       '11 a 10 ca', '22 a 10 ca', '10 a 64 ca', '2 a 85 ca', '1 a 70 ca',
       '10 a 64 ca', '35 a 10 ca', '18 a 25 ca', '18 a 70 ca'],
      dtype=object)

print(ref_parcelle_to_parts(df_plots.idu))
print(superficie_from_str(df_plots.superficie_ha))
print(superficie_ha_a_ca(df_plots.superficie_m2))
print(superficie_ha_a_ca(df_plots_na_none.superficie_m2))
print(superficie_ha_a_ca(df_only_one_na.superficie_m2))
print(superficie_ha_a_ca(df_only_one.superficie_m2))
print(superficie_from_str(arr))


