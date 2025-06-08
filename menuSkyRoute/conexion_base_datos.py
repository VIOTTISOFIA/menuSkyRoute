# conexion_base_datos.py
import mysql.connector

#Importa configuracion
from config import DB_CONFIG


# Funcion para conectar y cerrar conexion a la DB.
def conectar():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        return conexion
    except mysql.connector.Error as e:
        print(f"Error de conexión: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
