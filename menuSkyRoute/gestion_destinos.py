import mysql.connector
#from menuSkyRoute.conexion_base_datos import conectar, cerrar_conexion
from conexion_base_datos import conectar, cerrar_conexion


# Registrar un nuevo destino disponible
def agregar_destino():
    ciudad = input("Ingrese la ciudad: ")
    pais = input("Ingrese el país: ")
    costo_base = input("Ingrese el costo base: ")
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO destino (Ciudad, Pais, Costo_base) VALUES (%s, %s, %s)"
    valores = (ciudad, pais, costo_base)
    cursor.execute(query, valores)
    conexion.commit()
    cerrar_conexion(conexion)
    print("Destino agregado con éxito.")

# Listar todos los destinos disponibles
def listar_destinos():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM destino")
    resultados = cursor.fetchall()
    cerrar_conexion(conexion)

    for destino in resultados:
        print(f"{destino['ID_Destino']} | {destino['Ciudad']} | {destino['Pais']} |  {destino['Costo_base']}")

# Modificar datos de un destino por ID
def modificar_destino():
    id_destino = input("Ingrese el ID del destino a modificar: ")
    nueva_ciudad = input("Nueva ciudad: ")
    nuevo_pais = input("Nuevo país: ")
    nuevo_costo = input("Nuevo costo base: ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = """
        UPDATE destino
        SET Ciudad = %s, Pais = %s, Costo_base = %s
        WHERE ID_Destino = %s
    """
    valores = (nueva_ciudad, nuevo_pais, nuevo_costo, id_destino)
    cursor.execute(query, valores)
    conexion.commit()
    cerrar_conexion(conexion)
    print("Destino actualizado correctamente.")

# Eliminar un destino por ID
def eliminar_destino():
    id_destino = input("Ingrese el ID del destino a eliminar: ")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM destino WHERE ID_Destino = %s", (id_destino,))
    conexion.commit()
    cerrar_conexion(conexion)
    print("Destino eliminado.")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú de Gestión de Destinos ---")
        print("1. Agregar Destino")
        print("2. Listar Destinos")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_destino()
        elif opcion == "2":
            listar_destinos()
        elif opcion == "3":
            modificar_destino()
        elif opcion == "4":
            eliminar_destino()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()

