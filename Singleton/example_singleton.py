"""
El patrón de diseño Singleton es un patrón de software que garantiza que una
clase sólo tenga una única instancia y proporciona un punto de acceso global a
ella. En Python, esto se puede lograr mediante la creación de una clase con un
método new que devuelva la misma instancia cada vez que se llama.

En este ejemplo, se utiliza la variable de clase __instance para almacenar la
única instancia de la clase Singleton. Cada vez que se llama a Singleton(),
el método __new__ se ejecuta y devuelve Singleton.__instance si ya existe,
o crea una nueva instancia y la devuelve si no existe. De esta manera,
se garantiza que sólo exista una única instancia de la clase en todo momento.

"""
import sqlite3

class DatabaseConnection:
    __instance = None

    def __new__(cls):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = object.__new__(cls)
        return DatabaseConnection.__instance

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self, database):
        if self.connection is None:
            self.connection = sqlite3.connect(database)
            self.cursor = self.connection.cursor()
            print("Connecting to the database...")
        else:
            print("Already connected to the database")
        return self.cursor


# Usage
conn = DatabaseConnection()
cursor = conn.connect("database.db")
print(cursor)  # <sqlite3.Cursor object at 0x...>

conn2 = DatabaseConnection()
cursor2 = conn2.connect("database.db")
print(cursor2)  # Already connected to the database
# <sqlite3.Cursor object at 0x...>

# ----------------------------------------------------------------------------
""" Mediante uso de un decorador, para que sea más 'pythonico'"""

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class DatabaseConnection:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self, database):
        if self.connection is None:
            self.connection = sqlite3.connect(database)
            self.cursor = self.connection.cursor()
            print("Connecting to the database...")
        else:
            print("Already connected to the database")
        return self.cursor


# Usage
conn = DatabaseConnection()
cursor = conn.connect("database.db")
print(cursor)  # <sqlite3.Cursor object at 0x...>

conn2 = DatabaseConnection()
cursor2 = conn2.connect("database.db")
print(cursor2)  # Already connected to the database
# <sqlite3.Cursor object at 0x...>

# ----------------------------------------------------------------------------
"""Impementación clasica de Singelton"""
class Singleton ():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print("Objeto Creado", s)

s1 = Singleton()
print("Objeto Creado", s1)
