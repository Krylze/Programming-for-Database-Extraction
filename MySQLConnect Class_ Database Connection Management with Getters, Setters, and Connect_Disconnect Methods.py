"""
Nombre: Karyylle Zia Legada
Grupo: 952
Desarrollar una clase llamada MySQLConnect que tenga como atributos: host, user, password, database.
Debe crear sus métodos set y get (property, setters).
	Debe tener los siguientes métodos:
conectar() : Debe conectarse a la base de datos usando los atributos, debe retornar el objeto de conexión.
desconectar(): Debe desconectar la base de datos. No debe retornar nada. Investigar método close().

"""
from mysql.connector import connect, Error


class MYSQLConnector:
    def __init__(self, host, user, password, database ):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, server):
        self.__host = server

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        self.__database = value


    def desconectar(self, connection):
        # Cerrar la conexión
        connection.close()


    def conectar(self):
            connection = connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database)
            return connection

    def desconectar(self, connection):
        connection.close()
        return

base = MYSQLConnector(host="localhost", user="root", password="DelaCruz1914", database="olimpiadas")

print(base.conectar())

