"""
Nombre: Karylle Zia
Grupo:952
Desarrollar una clase llamada ResultadosMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre.
Debe agregar los siguientes métodos:
insertar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Método para insertar datos en la Tabla Resultados, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
editar(oro, plata, bronce): Método para editar oro, plata, bronce en la Tabla Resultados. Validar que sean valores enteros positivos.
eliminar(idOlimpiada, idPais, idGenero): Método para eliminar un elemento de la Tabla Resultados. Debe tener como parámetro la llave primaria compuesta, retorna True si logró eliminarse y False en caso contrario.
consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Resultados. Ejemplo: “idPais = 1” , “idPais = 1 and idOlimpiada=2”

"""
from ejercicio1 import MYSQLConnector

class ResultadosMySQL (MYSQLConnector):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM resultados WHERE idOlimpiada = %s"
        cursor.execute(query, (idOlimpiada,))
        if cursor.fetchone() is not None:
            return False
        insert = "INSERT INTO resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert, (idOlimpiada, idPais, idGenero, oro, plata, bronce))
        conexion.commit()
        return True

    def editar(self, oro, plata, bronce, idOlimpiada):
        conexion = self.conectar()
        cursor = conexion.cursor()
        if oro < 0 or plata < 0 or bronce < 0:
            return False
        update = "UPDATE resultados SET oro = %s, plata = %s, bronce = %s WHERE idOlimpiada = %s"
        cursor.execute(update, (oro, plata, bronce, idOlimpiada))
        conexion.commit()
        return True

    def eliminar(self, idOlimpiada, idPais, idGenero):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
        cursor.execute(query, (idOlimpiada, idPais, idGenero))
        if cursor.fetchone() is None:
            return False
        delete = "DELETE FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
        cursor.execute(delete, (idOlimpiada, idPais, idGenero))
        conexion.commit()
        return True

    def consultar(self, filter):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM resultados WHERE" + filter
        cursor.execute(query)
        rest = cursor.fetchall(query)
        conexion.close()

        if rest is not None:
            return rest
        else:
            return False

pais_db = ResultadosMySQL(host="localhost", user="root", password="DelaCruz1914", database="olimpiadas")
#print(pais_db.insertar(1, 1, 5, 23, 145, 256))
#print(pais_db.editar(-2, 3, 5, 1))
print(pais_db.eliminar(1, 1, 5))