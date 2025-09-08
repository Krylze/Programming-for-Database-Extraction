"""
Nombre: Karylle Zia Legada
Grupo: 952
Realizar una función que reciba como parámetro un DataFrame y  retorne el porcentaje de valores nulos de cada columna.
Realizar una función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados.
Realizar una función que reciba como parámetro un DataFrame y un máximo porcentaje. Este debe eliminar todas las columnas que superen o igualen el máximo porcentaje de valores nulos establecidos en el DataFrame Original. Retornar la lista nombres de columnas eliminadas.  Validar que el porcentaje máximo esté entre 0 y 1.
Realizar una función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y una cadena. La cadena solo puede ser mean, bfill o ffill, en caso contrario lanzar una excepción. Debe sustituir los valores nulos por el método especificado y retornar el DataFrame modificado.
Realizar una función que reciba como parámetro un DataFrame y elimine los renglones repetidos en el DataFrame Original. Debe retornar la cantidad de renglones eliminados.

"""
import pandas as pd

d = {"A":[1, 3, 3, 4, 1],
     "B":[3, 4, 1, None, 3],
     "C":[3, 5, None, 9, 3],
     "D":[None, 3, 3, 6, None]}
ventas = pd.DataFrame(d)


def porcentajesValoresNulos (ventas):
    totalF = len(ventas)
    porcentajesNulos = (ventas.isnull().sum() / totalF) * 100
    return porcentajesNulos

res = porcentajesValoresNulos(ventas)
print(res) 