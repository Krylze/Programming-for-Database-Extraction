"""
Nombre: Karylle Zia legada
Grupo: 952
El archivo titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:
Generar un DataFrame con los datos del archivo.
Mostrar por pantalla las dimensiones del DataFrame.
Mostrar el número de datos que contiene, los nombres de sus columnas.
Mostrar las 10 primeras filas y las 10 últimas filas.
Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.

"""
import pandas as pd
df = pd.read_csv("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv")

vivos = df.loc[df["Survived"]==1].shape[0]
#.shape: obtener la forma o dimensiones del DataFrame
muertos = df.loc[df["Survived"]==0].shape[0]
porVivos = (vivos / len(df["Survived"])) * 100
porMuertos = (muertos / len(df["Survived"])) * 100

x = df.loc[df["Survived"]==1]
y = x.groupby('Pclass').size() / len(x) * 100


print("Las dimensiones del dataframe son:", df.shape)
print("\nLos nombres de las columnas son:", df.columns)
print("\n\nLas 10 primeras filas\n\n", df.head(11), "\n\nLas 10 últimas filas.\n\n", df.tail(11))
print("\n\nEl porcentaje de personas que sobrevivieron:", porVivos, "\n\nEl porcentaje de personas que muerieron:", porMuertos)
print("\n\nPorcentaje de personas que sobrevivieron en cada clase.", y)

