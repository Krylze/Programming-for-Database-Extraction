"""
Nombre: Karylle Zia
Grupo:952
Realizar una función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar
y una cadena. La cadena solo puede ser mean, bfill o ffill, en caso contrario lanzar una excepción.
Debe sustituir los valores nulos por el método especificado y retornar el DataFrame modificado.
"""
import pandas as pd

d = {"A": [1, 3, 3, 4, 1],
     "B": [3, 4, 1, None, 3],
     "C": [3, 5, None, 9, 3],
     "D": [None, 1, None, None, None]}
ventas = pd.DataFrame(d)

def sustituirValoresNulos(dataframe, columnas, metodo):
    if metodo not in ['mean', 'bfill', 'ffill']:
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'")

    for columna in columnas:
        if metodo == 'mean':
            mean_value = dataframe[columna].mean()
            dataframe[columna].fillna(mean_value, inplace=True)

        elif metodo == 'bfill':
            dataframe[columna].fillna(method='bfill', inplace=True)

        elif metodo == 'ffill':
            dataframe[columna].fillna(method='ffill', inplace=True)

    return dataframe

columnas_a_verificar = ["A", "B", "C", "D"]
metodo = "mean"
#metodo = "bfill"
#metodo = "ffill"

df_modificado = sustituirValoresNulos(ventas, columnas_a_verificar, metodo)
print(df_modificado)