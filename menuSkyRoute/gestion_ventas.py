import mysql.connector
from datetime import datetime
from conexion_base_datos import conectar, cerrar_conexion


# Registrar una nueva venta
def registrar_venta():
    cliente_id = input("Ingrese el ID del cliente: ")
    destino_id = input("Ingrese el ID del destino: ")
    fecha_venta = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    costo_total = input("Ingrese el costo total: ")
    estado = "2"  # Por defecto, la venta se registra como "Pendiente" en `ID_Estado_Venta`

    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO venta (ID_Cliente, ID_Destino, Fecha_venta, Costo_total, ID_Estado_Venta) VALUES (%s, %s, %s, %s, %s)"
    valores = (cliente_id, destino_id, fecha_venta, costo_total, estado)
    cursor.execute(query, valores)
    conexion.commit()
    cerrar_conexion(conexion)
    print("Venta registrada con estado Pendiente.")


# Listar todas las ventas registradas
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
        print(f"{venta['ID_Venta']} | Cliente: {venta['ID_Cliente']} | Destino: {venta['ID_Destino']} | Fecha: {venta['Fecha_venta']} |  {venta['Costo_total']} | Estado: {estado} | Fecha de anulación: {fecha_anulacion}")


# Modificar el estado de una venta
def modificar_estado_venta():
    id_venta = input("Ingrese el ID de la venta a modificar: ")
    print("\nEstados disponibles:")
    print("1. Confirmada")
    print("2. Pendiente")
    print("3. Cancelada")
    nuevo_estado = input("Ingrese el nuevo estado (1, 2 o 3): ")

    conexion = conectar()
    cursor = conexion.cursor()

    if nuevo_estado == "3":  # Si la venta se cancela, se registra la fecha de anulación
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


# Botón de arrepentimiento: anular la venta más reciente en estado Pendiente
def anular_venta_reciente():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT ID_Venta 
        FROM venta 
        WHERE ID_Estado_Venta = 2 
        ORDER BY Fecha_venta DESC 
        LIMIT 1
    """)
    venta = cursor.fetchone()

    if venta:
        id_venta = venta["ID_Venta"]
        fecha_anulacion = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("""
            UPDATE venta 
            SET ID_Estado_Venta = 3, Fecha_anulacion = %s 
            WHERE ID_Venta = %s
        """, (fecha_anulacion, id_venta))
        conexion.commit()
        print(f"Venta ID {id_venta} anulada exitosamente con fecha {fecha_anulacion}.")
    else:
        print("No hay ventas pendientes para anular.")

    cerrar_conexion(conexion)


# Menú interactivo
def menu():
    while True:
        print("\n--- Menú de Gestión de Ventas ---")
        print("1. Registrar Venta")
        print("2. Listar Ventas")
        print("3. Modificar Estado de Venta")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            modificar_estado_venta()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()
