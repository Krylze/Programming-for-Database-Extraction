"""
Nombre: Karylle Zia Legada
Fecha: Fecha: 16 de Agosto del 2023

Gestión de Pensionistas. Crear una clase llamada GrupoPensionistas la cual tendrá un único atributo una lista o
diccionario de objetos de tipo Pensionista (Elija a conveniencia si una lista o diccionario). Cada objeto de Pensionista
tiene los siguientes atributos: identificador del pensionista (string), un entero que indica la edad y una serie de
gastos mensuales que se guardan (lista de enteros). El número de gastos mensuales puede variar entre pensionistas.
Por ejemplo, el pensionista con identificador '1111A' se llama 'Carlos' tiene 68 años y tiene 3 gastos mensuales de 640, 589 y 573.
La clase GrupoPensionistas debe tener los siguientes métodos:

 mediaGastos(identificador) , dado el identificador o índice de un pensionista, devuelva el promedio de los gastos.
mediaEdad(), dado todos los pensionados, devuelve el promedio de las edades.
edadesExtremas(), dado todos los pensionados, devuelva al pensionado con menor y mayor edad en una tupla.
sumaPromedio(), dado todos los pensionados, devuelva la suma del promedio de los gastos de todos los pensionistas de la lista.
mediaMaxima(), dado todos los pensionistas, retorne el mayor promedio de los gastos entre todos los pensionistas de la lista, su nombre e identificador.
 gastoPromedio(lst), dado todos los pensionistas, devuelve una lista con el gasto promedio de cada persona. La lista resultante debe estar ordenada de forma ascendente.

"""
class Pensionista:
    def __init__(self, identificador, edad, gastos):
        self.identificador = identificador
        self.edad = edad
        self.gastos = gastos

class GrupoPensionistas:
    def __init__(self, pensionistas):
        self.pensionistas = pensionistas

    def mediaGastos(self, identificador):
        for pensionista in self.pensionistas:
            if pensionista.identificador == identificador:
                return sum(pensionista.gastos) / len(pensionista.gastos)
        return None

    def mediaEdad(self):
        edadTotal = 0
        for pensionista in self.pensionistas:
            edadTotal += pensionista.edad
        return edadTotal / len(self.pensionistas)

    def edadesExtremas(self):
        menorEdad = 1000
        mayorEdad = 0
        for pensionista in self.pensionistas:
            if pensionista.edad < menorEdad:
                menorEdad = pensionista.edad
            if pensionista.edad > mayorEdad:
                mayorEdad = pensionista.edad
        return menorEdad, mayorEdad

    def sumaPromedio(self):
        suma = 0
        for pensionista in self.pensionistas:
            suma += sum(pensionista.gastos) / len(pensionista.gastos)
        return suma

    def mediaMaxima(self):
        maxMedia = None
        maxPromedio = 0

        for pensionista in self.pensionistas:
            promedio_actual = sum(pensionista.gastos) / len(pensionista.gastos)

            if promedio_actual > maxPromedio:
                maxPromedio = promedio_actual
                maxMedia = (pensionista.identificador, maxPromedio)

        return maxMedia

    def gastoPromedio(self):
        gastoPromedio = []
        for pensionista in self.pensionistas:
            gastoPromedio.append(sum(pensionista.gastos) / len(pensionista.gastos))
        return sorted(gastoPromedio)


pensionista1 = Pensionista('1111A', 68, [640, 589, 573])
pensionista2 = Pensionista('1222A', 75, [360, 550, 376])
pensionista3 = Pensionista('1333A', 89, [250, 960, 850])

grupo = GrupoPensionistas([pensionista1, pensionista2, pensionista3])

print(grupo.mediaGastos('1111A'))
print(grupo.mediaEdad())
print(grupo.edadesExtremas())
print(grupo.sumaPromedio())
print(grupo.mediaMaxima())
print(grupo.gastoPromedio())
