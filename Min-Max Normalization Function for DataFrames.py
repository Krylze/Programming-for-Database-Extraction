"""
Nombre: Karylle Zia
Grupo: 952
Realizar una función que normalice los datos usando min-max que reciba como parámetro un DataFrame y otro parámetro
que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados.
"""

import pandas as pd

d = {"A":[17, 30, 34, 40, 15],
     "B":[32, 41, 19, 19, 33]}
edad = pd.DataFrame(d)


def normalizar(dataFrame, listacolumna):
    for i in listacolumna:
        maxValue = dataFrame[i].max()
        minValue = dataFrame[i].min()

        dataFrame["MinMax"] = (dataFrame[i] - minValue) / (maxValue - minValue)

    return dataFrame




print(normalizar(edad, ["A" , "B"] ))
