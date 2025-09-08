"""
Nombre: Karylle Zia Legada
Grupo: 952
Desarrollar una clase llamada OlimpiadaMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre.
Debe agregar los siguientes métodos:
insertar(id, year): Método para insertar datos en la Tabla Olimpiada, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
editar(year): Método para editar el año en la Tabla Olimpiada. Validar que el año no exista en la tabla.
eliminar(id): Método para eliminar un elemento de la Tabla Olimpiada. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Olimpiada. Ejemplo: “id = 1” , “year > 1990”

"""
from ejercicio1 import MYSQLConnector

class OlimpiadaMySQL (MYSQLConnector):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, year):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM olimpiada WHERE year_olimpiada = %s"
        cursor.execute(query, (year,))
        if cursor.fetchone() is not None:
            return False
        insert = "INSERT INTO olimpiada (id, year_olimpiada) VALUES (%s, %s)"
        cursor.execute(insert, (id, year))
        conexion.commit()
        conexion.close()
        return True

    def editar(self, newYear, year):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM olimpiada WHERE year_olimpiada = %s"
        cursor.execute(query, (year,))
        if cursor.fetchone() is None:
            return False
        else:
            update = "UPDATE olimpiada SET year_olimpiada = %s WHERE year_olimpiada = %s"
            cursor.execute(update, (newYear, year))
            conexion.commit()
            conexion.close()
            return True

    def eliminar(self, id):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM olimpiada WHERE id = %s"
        cursor.execute(query, (id,))
        if cursor.fetchone() is None:
            return False
        else:
            delete = "DELETE FROM olimpiada WHERE id = %s"
            cursor.execute(delete,(id,))
            conexion.commit()
            conexion.close()
            return True

    def consultar (self, filter):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM olimpiada WHERE" + filter
        cursor.execute(query)
        rest = cursor.fetchall(query)
        conexion.close()

        if rest is not None:
            return rest
        else:
            return False


pais_db = OlimpiadaMySQL(host="localhost", user="root", password="DelaCruz1914", database="olimpiadas")

print(pais_db.insertar(1, 1912))
print(pais_db.insertar(2, 1915))
print(pais_db.insertar(3, 1927))
#print(pais_db.editar(1914, 1912))
#print(pais_db.eliminar(1))