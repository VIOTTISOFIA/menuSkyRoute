# conexion_base_datos.py
import mysql.connector
from menuSkyRoute.config import DB_CONFIG


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
