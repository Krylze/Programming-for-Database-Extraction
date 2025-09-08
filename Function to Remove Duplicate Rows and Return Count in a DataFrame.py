"""
Nombre: Karylle Zia
Grupo:952
Realizar una función que reciba como parámetro un DataFrame y elimine los renglones repetidos en el DataFrame Original.
Debe retornar la cantidad de renglones eliminados.

"""

import pandas as pd

d = {"A": [1, 3, 3, 4, 1],
     "B": [3, 4, 1, None, 3],
     "C": [3, 5, None, 9, 3],
     "D": [None, 1, None, None, None]}
ventas = pd.DataFrame(d)

def elimRenglonesDupli(dataframe):
    cantInc = len(dataframe)
    dataframe = dataframe.drop_duplicates()
    cantElim = cantInc - len(dataframe)

    return cantElim

renElim = elimRenglonesDupli(ventas)
print("Cantidad de renglones eliminados:", renElim)