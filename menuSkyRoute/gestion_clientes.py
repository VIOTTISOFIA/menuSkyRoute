"""
Modulo: Gestión de Clientes
Sistema de gestion de clientes, con conexion MySQL que
permite operaciones CRUD sobre la tabla.

Funciones:
agregar_cliente(): Solicita al usuario la razón social, CUIT y correo electrónico para añadir un nuevo cliente a la base de datos.
listar_clientes(): Muestra todos los clientes registrados en la base de datos, incluyendo su ID, razón social, CUIT y correo.
modificar_cliente(): Permite actualizar la información de un cliente existente buscando por su ID.
eliminar_cliente(): Elimina un cliente de la base de datos utilizando su ID.
menu(): Proporciona una interfaz interactiva basada en consola.
"""


import mysql.connector
#from menuSkyRoute.conexion_base_datos import conectar, cerrar_conexion
from conexion_base_datos import conectar, cerrar_conexion


# Agregar un nuevo cliente
def agregar_cliente():
    razon_social = input("Ingrese la razón social: ")
    cuit = input("Ingrese el CUIT: ")
    correo = input("Ingrese el correo: ")
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO cliente (Razon_Social, CUIT, Correo) VALUES (%s, %s, %s)"
    valores = (razon_social, cuit, correo)
    cursor.execute(query, valores)
    conexion.commit()
    cerrar_conexion(conexion)
    print("Cliente agregado con éxito.")

# Listar todos los clientes registrados
def listar_clientes():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cliente")
    resultados = cursor.fetchall()
    cerrar_conexion(conexion)

    for cliente in resultados:
        print(f"{cliente['ID_Cliente']} | {cliente['Razon_Social']} | CUIT: {cliente['CUIT']} | {cliente['Correo']}")

# Modificar datos de un cliente por ID
def modificar_cliente():
    id_cliente = input("Ingrese el ID del cliente a modificar: ")
    nueva_razon = input("Nueva razón social: ")
    nuevo_cuit = input("Nuevo CUIT: ")
    nuevo_correo = input("Nuevo correo: ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = """
        UPDATE cliente
        SET Razon_Social = %s, CUIT = %s, Correo = %s
        WHERE ID_Cliente = %s
    """
    valores = (nueva_razon, nuevo_cuit, nuevo_correo, id_cliente)
    cursor.execute(query, valores)
    conexion.commit()
    cerrar_conexion(conexion)
    print("Cliente actualizado correctamente.")

# Eliminar un cliente por ID
def eliminar_cliente():
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM cliente WHERE ID_Cliente = %s", (id_cliente,))
    conexion.commit()
    cerrar_conexion(conexion)
    print("Cliente eliminado.")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú de Gestión de Clientes ---")
        print("1. Agregar Cliente")
        print("2. Listar Clientes")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()

