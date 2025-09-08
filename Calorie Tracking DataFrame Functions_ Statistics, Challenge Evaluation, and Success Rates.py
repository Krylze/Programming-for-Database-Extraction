"""
Crear un programa que contenga las siguientes funciones:
a. 	Crear una función que retorne un DataFrame indexado, con la siguiente Información: (5%)
b. 	Crear una función que reciba como parámetro el Data Frame anterior, y retorne la media, mediana y desviación estándar
de ambas columnas. (5%)
c. 	Desarrollar una función que agregue otra columna al Data Frame para ver si se ha cumplido el reto de quemar más de
400 calorías por hora (Calorías/Tiempo > 400/60). El Data Frame resultante debe ser el siguiente: (5%)
d. 	Crear una función que retorne el porcentaje de días que se ha conseguido el reto y los que no. (10%)

"""

import pandas as pd

data = {
    'Día': ['L', 'M', 'X', 'J', 'V'],
    'Calorías': [420, 380, 390, 490, 300],
    'Tiempo': [60, 40, 75, 55, 45]
}

def Index():
    df = pd.DataFrame(data).set_index('Día')
    return df


def calStats(df):
    stats = {
        'Mean Calories': df['Calorías'].mean(),
        'Median Calories': df['Calorías'].median(),
        'Std Calories': df['Calorías'].std(),
        'Mean Time': df['Tiempo'].mean(),
        'Median Time': df['Tiempo'].median(),
        'Std Time': df['Tiempo'].std()
    }
    return pd.Series(stats)


def addColumn(df):
    df["Reto"]= df["Calorías"]/df["Tiempo"] > 400/60
    return df


def poorcentaje(df):
    completed = df['Reto'].sum()
    total = df['Reto'].count()
    percentage = (completed / total) * 100
    return percentage

# Apply the functions and print the outputs
stats = calStats(Index())
df_challenge = addColumn(Index())
percent = poorcentaje(df_challenge)



print(Index())
print(stats)
print(df_challenge)
print(stats)