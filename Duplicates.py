"""
Nombre: Karylle Zia Legada
Fecha: 16 de Agosto del 2023

Duplicados. Dada una lista de números enteros, retorna
True si al menos un valor aparece dos veces, y Falso si todos los elementos son distintos.

Ejemplos:
nums = [1, 2, 3, 1]
duplicados(nums)
True

nums = [1, 2, 3, 4]
duplicados(nums)
False

"""


def numeros(lista):
    return len(lista) != len(set(lista))


lista = [1, 2, 4, 4]
print("En la lista hay numeros repetidos:", numeros(lista))
