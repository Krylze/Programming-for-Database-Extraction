"""
Nombre:Karylle Zia
Grupo: 952
Realizar una función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados.
"""
import pandas as pd

d = {"A":[1, 3, 3, 4, 1],
     "B":[3, 4, 1, None, 3],
     "C":[3, 5, None, 9, 3],
     "D":[None, 3, 3, 6, None]}
ventas = pd.DataFrame(d)

dupli = ventas.duplicated()
print(dupli)