"""
Se tiene un archivo llamado titanic.csv, el cual contiene la lista de los pasajeros del Titanic.
Escribir un función que limpie los datos con los siguientes requisitos:
a. 	Generar un dataframe con los datos del archivo. (3%)
b. 	Imprimir el porcentaje de valores nulos de la columna Age(Edad). (2%)
c. 	Eliminar del DataFrame los pasajeros con edad desconocida. (5%)
d. 	Imprimir el porcentaje de valores nulos de la columna Cabin. (5%)
e. 	Sustituir en el DataFrame los valores desconocidos de la columna Cabin, por la frase “Sin especificar”. (5%)
f.  	Retornar el DataFrame con los cambios realizados. (5%)

"""
import pandas as pd

def dataFrame():
    df = pd.read_csv("datasets/titanic.csv", sep=",")

    nulos = (df["Age"].isnull().sum() / len(df)) * 100
    print("El porcentaje de edades con valores nulos: ", nulos)

    edadDesconocido = df.dropna(subset=["Age"])

    nulosCabin = (df["Cabin"].isnull().sum() / len(df)) * 100
    print("Procentaje de valores de la columna cabin: ", nulosCabin)

    edadDesconocido["Cabin"] = edadDesconocido["Cabin"].fillna("Sin especificar")
    return edadDesconocido


print(dataFrame())



