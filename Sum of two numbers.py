"""
Nombre: Karylle Zia Legada
Fecha: 16 de Agosto del 2023

Suma de dos números. Dado una lista de números enteros y un valor entero (target), retorna el índice de los dos números
que sumados sean igual al target. Debe asumir que existe siempre una única solución, y que los elementos no se pueden
usar dos veces. Debes retornar una tupla con los índices.
Ejemplos:

nums = [2, 7, 11, 15]
target = 9
busquedaSuma(nums, target)
(0, 1)

nums = [3, 2, 4]
target = 6
busquedaSuma(nums, target)
(1, 2)

"""

nums = [2, 3, 11, 15, 7]

def SumaDeDosNumeros(nums, target):
  dic = {}
  for indice, value in enumerate(nums):
    res = target - value
    if res in dic:
      return (dic[res], indice)
    else:
      dic[value] = indice
  return None


print(SumaDeDosNumeros(nums,9))