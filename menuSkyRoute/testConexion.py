import sys
import os

# Agrega el directorio raíz del proyecto al path de búsqueda
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from menuSkyRoute.conexion_base_datos import conectar, cerrar_conexion



# test_conexion.py
from menuSkyRoute.conexion_base_datos import conectar, cerrar_conexion

# 1. Conectar a la base de datos
conexion = conectar()

# 2. Verificar si la conexión fue exitosa
if conexion and conexion.is_connected():
    print(f"✅ Conexión exitosa a {conexion.server_host}")

    # 3. Ejecutar consulta para mostrar tablas
    cursor = conexion.cursor()
    cursor.execute("SHOW TABLES")
    tablas = cursor.fetchall()
    print("📋 Tablas disponibles:")
    for tabla in tablas:
        print(f" - {tabla[0]}")
    
    cursor.close()
    cerrar_conexion(conexion)
else:
    print("❌ Error al conectar a la base de datos")
