"""
Nombre: Karylle Zia legada
Grupo: 952
El archivo cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas:
nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la
acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre
de bolsa), Efectivo (capitalización al cierre en miles de euros). Construir una función que construya un DataFrame
a partir del archivo con el formato anterior y devuelve otro DataFrame con el mínimo, el máximo y la media de cada columna.
"""
import pandas as pd

df = pd.read_csv("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv", sep=";",
                     decimal=",")
def estadisticas():
    maximo = df.select_dtypes(include=[int, float]).max()
    minimo = df.select_dtypes(include=[int, float]).min()
    promedio = df.select_dtypes(include=[int, float]).mean()
    res = pd.DataFrame({'Mínimo': minimo, 'Máximo': maximo, 'Promedio': promedio})
    return res

print(df)
print("\n\n")
print(estadisticas())