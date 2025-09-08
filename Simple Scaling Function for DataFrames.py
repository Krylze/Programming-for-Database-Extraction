"""
Nombre: Karylle Zia
Grupo: 952
Realizar una función que normalice los datos usando escalado simple que reciba como parámetro un DataFrame y otro
parámetro que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados.
"""

import pandas as pd

d = {"A":[17, 30, 34, 40, 15],
     "B":[32, 41, 19, 19, 33],
     }
edad = pd.DataFrame(d)

def EscalaSimple (dataframe, listacolumnas):
    for i in listacolumnas:
        dataframe["maxi"] = dataframe[i] / dataframe[i].max()

    return dataframe["maxi"]

print(EscalaSimple(edad,["A", "B"]))
