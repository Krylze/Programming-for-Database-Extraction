"""
El archivo bitcoin-tweets.csv, contiene los tweets obtenidos en una búsqueda en Twitter sobre bitcoins, se pide lo siguiente:
a. 	Crear una función que permita guardar el contenido del archivo en una tabla de Base de Datos. Debe asumir que existe
una Base de Datos llamada Twitter,  la cual contiene una tabla Twitter_Bitcoins donde debe guardar la información. (10%)
b. 	Crear una función que se conecte a la base de datos y lea toda la información de la tabla Twitter_Bitcoins y retorne
un DataFrame creado a partir de la información de la tabla. (10%)
c. 	Crear una función que retorne los twitts con más likes. La función debe de tener como parámetro la cantidad de
twitts a retornar. Si el parámetro es un 3 debe retornar los tres con mayor número de likes. Si es un 5 debe retornar
los cinco con mayor número de likes. Validar que el número no sea mayor a la cantidad de datos. NOTA: Debe tomar en
cuenta que esta función se conecta a la base de datos, es decir asume que los datos ya se encuentran en la tabla correspondiente. (5%)

"""
import pandas as pd
from sqlalchemy import create_engine

user = "root"
password = "DelaCruz1914"
bd = "twitter"
cadenaConexion = f"mysql+mysqlconnector://{user}:{password}" \
                 f"@localhost/{bd}"

engine = create_engine(cadenaConexion)
conexion = engine.connect()
#print(cadenaConexion)

df = pd.read_csv("datasets/bitcoin-tweets.csv", sep=";")
#print(df.head())

def Guardar():
    df.to_sql("twitter_bitcoin", conexion, index=False)


def Read(nombreTabla):
    engine=create_engine(cadenaConexion)
    conexion=engine.connect()

    Query = f"SELECT * FROM {nombreTabla}"
    df = pd.read_sql_query(Query,conexion)
    conexion.close()
    return df

def Likes (cantidad):
    engine=create_engine(cadenaConexion)
    conexion=engine.connect()
    Query = f"SELECT * FROM twitter_bitcoin ORDER BY LIKES DESC LIMIT {cantidad}"
    df = pd.read_sql_query(Query, conexion)
    return df

#print(Read("twitter_bitcoin"))
print(Likes(5))









