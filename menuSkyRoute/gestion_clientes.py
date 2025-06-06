import mysql.connector
from menuSkyRoute.conexion_base_datos import conectar, cerrar_conexion

# Lista temporal de clientes (si necesitás manipular en memoria)
clientes_temporales = []

# Agregar un nuevo cliente
def agregar_cliente(razon_social, cuit, correo):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO cliente (Razon_Social, CUIT, Correo) VALUES (%s, %s, %s)"
    valores = (razon_social, cuit, correo)
    cursor.execute(query, valores)
    conexion.commit()
    cerrar_conexion(conexion)
    print("✅ Cliente agregado con éxito.")

# Listar todos los clientes registrados
def listar_clientes():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cliente")
    resultados = cursor.fetchall()
    cerrar_conexion(conexion)

    # Iterar sobre los resultados correctamente
    for cliente in resultados:
        print(f"🆔 {cliente['ID_Cliente']} | 🏢 {cliente['Razon_Social']} | 💼 CUIT: {cliente['CUIT']} | ✉️ {cliente['Correo']}")

    return resultados  # Esto estaba mal posicionado antes

# Modificar datos de un cliente por ID
def modificar_cliente(id_cliente, nueva_razon, nuevo_cuit, nuevo_correo):
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
    print("✏️ Cliente actualizado correctamente.")

# Eliminar un cliente por ID
def eliminar_cliente(id_cliente):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM cliente WHERE ID_Cliente = %s", (id_cliente,))
    conexion.commit()
    cerrar_conexion(conexion)
    print("🗑️ Cliente eliminado.")
