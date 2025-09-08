"""
Se tienen los archivos emisiones-2017.csv, emisiones-2018.csv, emisiones-2019.csv, los cuales contienen datos sobre las emisiones contaminantes de los años 2017, 2018 y 2019. Escribir las siguientes funciones:
a. 	Realizar una función que retorne un DataFrame con la información de todos los archivos,  debe incluir todo lo siguiente:
i. 	Solo tener las siguientes columnas: Estación, Magnitud, Año, Mes y las correspondientes a los días D01, D02, D03, etc. (5%)
ii.	 Debe reestructurar el Data Frame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna. NOTA: Investigar función melt. (5%)
iii.   Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime) (5%)
iv.  Eliminar los renglones con fechas no válidas (puede utilizar la función isnat del módulo numpy) y ordenar el Data Frame por estaciones contaminantes y fecha. (5%)
b. 	Crear una función que reciba una estación, una magnitud (contaminante) y un rango de fechas. Debe retornar una serie con las emisiones de la magnitud(contaminante) dado en la estación y rango de fechas dado. (5%)

"""
import pandas as pd

def union(archivos):
    df = pd.concat([pd.read_csv(archivo, sep=';') for archivo in archivos], ignore_index=True)
    columnDias = [f'D{i:02d}' for i in range(1, 32)]
    df = df[['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + columnDias]
    df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], value_vars=columnDias,
                 var_name='DIA', value_name='VALOR')
    df['ANO'] = df['ANO'].astype(int)
    df['MES'] = df['MES'].astype(int)
    df['DIA'] = df['DIA'].str[1:].astype(int)
    df['FECHA'] = pd.to_datetime({'year': df['ANO'], 'month': df['MES'], 'day': df['DIA']}, errors='coerce')
    df = df.dropna(subset=['FECHA'])
    df = df.sort_values(by=['ESTACION', 'FECHA'])
    return df

def filter(df, estacion, magnitud, fechaInicio, fecha_fin):
    filtro = (df['ESTACION'] == estacion) & (df['MAGNITUD'] == magnitud)
    fechaInicio = pd.to_datetime(fechaInicio)
    fecha_fin = pd.to_datetime(fecha_fin)
    filtro &= (df['FECHA'] >= fechaInicio) & (df['FECHA'] <= fecha_fin)
    return df.loc[filtro, 'VALOR']

archivos = ['datasets/emisiones-2017.csv', 'datasets/emisiones-2018.csv', 'datasets/emisiones-2019.csv']
df_unificado = union(archivos)


print(df_unificado.head())


emisiones_filtradas = filter(df_unificado, estacion=4, magnitud=1,
                             fechaInicio='2018-01-01', fecha_fin='2018-12-31')

# Imprimir los resultados del filtro
print(emisiones_filtradas)