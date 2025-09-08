"""
Nombre: Karylle Zia Legada
Fecha: Fecha: 16 de Agosto del 2023

Estadística Básica. Cree una clase llamada Estadística que contiene como atributo una lista de números naturales la cual
puede contener repetidos. Debe contener los siguientes métodos:
Frecuencia de Números. Dada la lista, devuelve un diccionario con el número de veces que aparece cada número en la lista.
Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.
Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores.
Ejemplo:
		lista = ListaNumeros ([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
		lista.histograma()

		Salida:
1 *****
2 ******
3 ****
4 **

"""
class Estadistica():

    def __init__(self, numeros):
        self.numeros = numeros

    def FrecuenciaNumeros(self):
        dic = {}
        for value in self.numeros:
            if value in dic:
                dic[value]+=1
            else:
                dic[value] = 1
        return dic

    def Moda(self):
        dic = self.FrecuenciaNumeros()
        maximo = 0
        moda = 0
        for value in dic:
            if dic[value] > maximo:
                maximo = dic[value]
                moda = value
        return moda

    def Histograma(self):
        dic = self.FrecuenciaNumeros()
        for value in dic:
            print(value, "*" * dic[value])

lista = Estadistica([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
print(lista.FrecuenciaNumeros())
print(lista.Moda())
print(lista.Histograma())
