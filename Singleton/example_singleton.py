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


"""Todos los módulos son Singleton por defecto debido al comportamiento de
importación de Python. Python funciona de la siguiente manera:

1 - Verifica si un módulo de Python ha sido importado.
2 - Si ha sido importado, devuelve el objeto para el módulo. Si no ha sido
importado, lo importa e instancia.
Entonces, cuando se importa un módulo, se inicializa. Sin embargo, cuando se
importa el mismo módulo nuevamente, no se inicializa de nuevo, lo que se
relaciona con el comportamiento Singleton de tener solo un objeto y devolver
el mismo objeto."""
# ----------------------------------------------------------------------------
"""Comencemos con una breve introducción a las metaclases. Una metaclase es
una clase de una clase, lo que significa que la clase es una instancia de su
metaclase. Con las metaclases, los programadores tienen la oportunidad de
crear clases de su propio tipo a partir de las clases predefinidas de Python.
Por ejemplo, si tienes un objeto llamado MyClass, puedes crear una metaclase
llamada MyKls que redefine el comportamiento de MyClass de la manera que necesites.
Vamos a entender esto en detalle.

En Python, todo es un objeto. Si decimos a=5, entonces type(a) devuelve <type 'int'>,
lo que significa que a es del tipo int. Sin embargo, type(int) devuelve <type 'type'>,
lo que sugiere la presencia de una metaclase ya que int es una clase del tipo type."""

class MyInt(type):
    def __call__(cls , *args, **kwds):
        print("*** Aquí está mi INT", args)
        print("Aquí va cualquier cosa que quieras con este objeto")
        return type.__call__(cls, *args, **kwds)

class int(metaclass = MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4, 5)
# ----------------------------------------------------------------------------
"""Otro ejemplo de uso en el mundo real: en el caso de implementación de servicios
de checkhealt para nuestra infrestructura. Creamos la clase HealtCHeck, que se
implementa como un Singleton. También mantenemos una lista de servidores contra
los cuales se necesita ejecutra la verificación. Si se elimina un servidor de la
lista, el software de ferificacioón debe detectarlo y eliminarlo de los servidores
configurados para la verificación.
En el siguiente código, los objetos hc1 y hc2 son iguales a la clase Singleton.
Se añanden servidores a la infrestructura para la verificación con el método
addServer(). Primero, se ejecuta la iteración de la verificación de salud contra
estos servidores. El método cahgeServer() elimina el último servidro y añade uno nuevo
a la infrastructura programada para la verificación. Entonces, cuando se ejecuta
la verificación en la segunda iteración, toma la lista modificada de servidores."""

class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self) -> None:
        self._servers = []

    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 3")
        self._servers.append("Server 5")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
print("Hora de checkear server (1)..")
for i in range(4):
    print("Checkeando ", hc1._servers[i])


hc2.addServer()
print("Hora de checkear server (2)..")
for i in range(4):
    print("Checkeando ", hc1._servers[i])
