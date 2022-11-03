import sys
import sqlite3
from sqlite3 import Error


try:
    with sqlite3.connect("Evidencia_3.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Reservaciones (ID_Reservacion INTEGER PRIMARY KEY, ID_Cliente INTEGER NOT NULL, ID_Sala INTEGER, nombre_evento TEXT, Turno TEXT, fecha_evento timestamp);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Clientes (ID_Cliente INTEGER PRIMARY KEY, nombre TEXT);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Salas (ID_Sala INTEGER NOT NULL, cupo INTEGER);")
        print("Tabla creada exitosamente")
except Error as e:
    print(e)
except:
    print(f"se produjo el siguiente error: {sys.exc_info()[0]}")