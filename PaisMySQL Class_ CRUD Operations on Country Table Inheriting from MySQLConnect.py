"""
Nombre: Karylle Zia Legada
Grupo: 952
Desarrollar una clase llamada PaisMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre.
Debe agregar los siguientes métodos:
insertar(id, nombre): Método para insertar datos en la Tabla Pais, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
editar(nombre): Método para editar el nombre en la Tabla País. Validar que nombre no exista en la tabla.
eliminar(id): Método para eliminar un elemento de la Tabla País. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla País. Ejemplo: “id = 1” , “nombre like %A%”

"""
from ejercicio1 import MYSQLConnector

class PaisMySQL(MYSQLConnector):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, nombre):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM Pais WHERE nombre = %s"
        cursor.execute(query, (nombre,))
        if cursor.fetchone() is not None:
            return False
        insert = "INSERT INTO Pais (id, nombre) VALUES (%s, %s)"
        cursor.execute(insert, (id, nombre))
        conexion.commit()
        conexion.close()
        return True

    def editar(self, nombre, nuevo_nombre):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM Pais WHERE nombre = %s"
        cursor.execute(query, (nombre,))
        if cursor.fetchone() is None:
            return False
        else:
            update = "UPDATE Pais SET nombre = %s WHERE nombre = %s"
            cursor.execute(update, (nuevo_nombre, nombre))
            conexion.commit()
            conexion.close()
            return True

    def eliminar(self, id):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM Pais WHERE id = %s"
        cursor.execute(query, (id,))
        if cursor.fetchone() is None:
            return False
        else:
            delete = "DELETE FROM Pais WHERE id = %s"
            cursor.execute(delete,(id,))
            conexion.commit()
            conexion.close()
            return True

    def consultar(self, filter):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM Pais WHERE " + filter
        cursor.execute(query)
        resultado = cursor.fetchall()
        conexion.close()

        if resultado is not None:
            return resultado
        else:
            return False





pais_db = PaisMySQL(host="localhost", user="root", password="DelaCruz1914", database="olimpiadas")

#print(pais_db.insertar(153, "Mangolandia3"))
#print(pais_db.editar("Mangolandia3", "Mangolandia2"))
#print(pais_db.eliminar(153))

print(pais_db.consultar("nombre like '%a%'"))