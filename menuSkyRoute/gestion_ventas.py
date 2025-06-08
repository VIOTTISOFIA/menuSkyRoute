"""
modulo: Gestión de Ventas

Funciones para gestionar las ventas de SkyRoute, 
interaccion con la base de datos que permite registar, listar y modificar su estado.
Incluye boton de arrepentiemiento.

Funciones
registrar_venta(): Permite registrar una nueva venta asociándola a un cliente y un destino, ingresando la fecha y el costo total. 
listar_ventas(): Muestra un listado detallado de todas las ventas registradas y datos asociados.
modificar_estado_venta(): Permite cambiar el estado de una venta existente (a Confirmada, Pendiente o Cancelada) utilizando su ID. 
anular_venta_reciente(): Esta función actúa como un "botón de arrepentimiento"
menu(): Proporciona una interfaz de consola interactiva para que el usuario pueda elegir entre las diferentes operaciones de gestión de ventas.
"""

import mysql.connector
from datetime import datetime, timedelta, date
from conexion_base_datos import conectar, cerrar_conexion

# Registrar una nueva venta
def registrar_venta():
    cliente_id = input("Ingrese el ID del cliente: ")
    destino_id = input("Ingrese el ID del destino: ")
    fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha automática
    costo_total = input("Ingrese el costo total: ")
    estado = "2"  # Por defecto, la venta se registra como "Pendiente"

    conexion = conectar()
    cursor = conexion.cursor()
    query = """
        INSERT INTO venta (ID_Cliente, ID_Destino, Fecha_venta, Costo_total, ID_Estado_Venta)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (cliente_id, destino_id, fecha_venta, costo_total, estado)
    cursor.execute(query, valores)
    conexion.commit()
    cerrar_conexion(conexion)
    print("Venta registrada con estado Pendiente.")

# Listar todas las ventas
def listar_ventas():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT v.ID_Venta, v.ID_Cliente, v.ID_Destino, v.Fecha_venta, 
            v.Costo_total, e.Tipo_estado, v.Fecha_anulacion 
        FROM venta v 
        INNER JOIN estado_venta e ON v.ID_Estado_Venta = e.ID_Estado_Venta
    """)
    resultados = cursor.fetchall()
    cerrar_conexion(conexion)

    for venta in resultados:
        estado = venta['Tipo_estado']
        fecha_anulacion = venta.get('Fecha_anulacion', 'N/A')
        print(f"{venta['ID_Venta']} | Cliente: {venta['ID_Cliente']} | Destino: {venta['ID_Destino']} | "
            f"Fecha: {venta['Fecha_venta']} | {venta['Costo_total']} | Estado: {estado} | "
            f"Fecha de anulación: {fecha_anulacion}")

# Modificar estado de venta
def modificar_estado_venta():
    id_venta = input("Ingrese el ID de la venta a modificar: ")
    print("\nEstados disponibles:")
    print("1. Confirmada")
    print("2. Pendiente")
    print("3. Cancelada")
    nuevo_estado = input("Ingrese el nuevo estado (1, 2 o 3): ")

    if nuevo_estado not in {"1", "2", "3"}:
        print("Estado no válido.")
        return

    conexion = conectar()
    cursor = conexion.cursor()

    if nuevo_estado == "3":
        fecha_anulacion = input("Ingrese la fecha de anulación (YYYY-MM-DD): ")
        query = "UPDATE venta SET ID_Estado_Venta = %s, Fecha_anulacion = %s WHERE ID_Venta = %s"
        valores = (nuevo_estado, fecha_anulacion, id_venta)
    else:
        query = "UPDATE venta SET ID_Estado_Venta = %s WHERE ID_Venta = %s"
        valores = (nuevo_estado, id_venta)

    cursor.execute(query, valores)
    conexion.commit()
    cerrar_conexion(conexion)
    print("Estado de la venta actualizado correctamente.")

# Botón de arrepentimiento (simula cancelación dentro de 60 días pero en 60 segundos)
def anular_venta_reciente():
    print("\nActivando Botón de Arrepentimiento...")
    id_venta = input("Ingrese el ID de la venta a cancelar: ")

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT Fecha_venta, ID_Estado_Venta FROM venta WHERE ID_Venta = %s", (id_venta,))
    venta = cursor.fetchone()

    if not venta:
        print("Venta no encontrada.")
        cerrar_conexion(conexion)
        return

    fecha_venta = venta['Fecha_venta']
    estado_actual = venta['ID_Estado_Venta']
    ahora = datetime.now()

    # Convertir fecha si viene como string o date
    if isinstance(fecha_venta, str):
        try:
            fecha_venta = datetime.strptime(fecha_venta, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            fecha_venta = datetime.strptime(fecha_venta, "%Y-%m-%d")
    elif isinstance(fecha_venta, date):
        fecha_venta = datetime.combine(fecha_venta, datetime.min.time())

    tiempo_transcurrido = (ahora - fecha_venta).total_seconds()

    if tiempo_transcurrido <= 60:  # Simulación: 60 segundos = 60 días
        if estado_actual == 3:
            print("La venta ya está cancelada.")
        else:
            cursor.execute("""
                UPDATE venta 
                SET ID_Estado_Venta = 3, Fecha_anulacion = %s 
                WHERE ID_Venta = %s
            """, (ahora, id_venta))
            conexion.commit()
            print("Venta anulada correctamente dentro del tiempo permitido (simulación de 60 días).")
    else:
        print("Ha pasado el tiempo establecido por la política de la empresa para anular esta venta.")

    cerrar_conexion(conexion)

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Gestión de Ventas ---")
        print("1. Registrar Venta")
        print("2. Listar Ventas")
        print("3. Modificar Estado de Venta")
        print("4. Activar Botón de Arrepentimiento")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            modificar_estado_venta()
        elif opcion == "4":
            anular_venta_reciente()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar menú
if __name__ == "__main__":
    menu()

