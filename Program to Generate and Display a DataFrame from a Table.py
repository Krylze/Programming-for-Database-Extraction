"""
Nombre: Karylle Zia legada
Grupo: 952
Escribir un programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
"""
import pandas as pd
df =pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [30500, 35600, 28300, 33900],
    "Gastos": [22000, 23400, 18100, 20700]
})

def calcular():
    df["Resultado"] = df["Ventas"] - df["Gastos"]
    return df[["Mes", "Resultado"]]

print(df)

res = calcular()
print("")
resultadoFiltrado = res.loc[res["Mes"].isin(["Febrero", "Marzo"]), ["Mes", "Resultado"]]
print(resultadoFiltrado)