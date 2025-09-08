"""
Nombre: Karylle Zia
Grupo: 952
Realizar una función que reciba como parámetro un DataFrame y un máximo porcentaje. Este debe eliminar todas las columnas
que superen o igualen el máximo porcentaje de valores nulos establecidos en el DataFrame Original.
Retornar la lista nombres de columnas eliminadas.  Validar que el porcentaje máximo esté entre 0 y 1.

"""
import pandas as pd

d = {"A": [1, 3, 3, 4, 1],
     "B": [3, 4, 1, None, 3],
     "C": [3, 5, None, 9, 3],
     "D": [None, 1, None, None, None]}
ventas = pd.DataFrame(d)


def eliminarColumnasNulos(ventas, maxporcen):
    if maxporcen < 0 or maxporcen > 1:
        raise ValueError("El porcentaje máximo debe estar entre 0 y 1")

    totalF = len(ventas)
    valoresNulos = ventas.isnull().sum()
    porcentNulos = (valoresNulos / totalF)
    columnsElim = porcentNulos[porcentNulos >= maxporcen].index.tolist()

    return columnsElim

columnsElim = eliminarColumnasNulos(ventas, 0.3)
print("Columnas eliminadas:", columnsElim)
