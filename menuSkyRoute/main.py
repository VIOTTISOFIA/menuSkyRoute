"""
Sistema de Gestión de Pasajes
Este script main.py es el punto de entrada principal para el sistema de gestión de pasajes SkyRoute. 
Centraliza las operaciones de gestión de clientes, destinos y ventas, 
permitiendo al usuario navegar entre las diferentes funcionalidades del sistema.
"""

# main.py

import gestion_clientes
import gestion_destinos
import gestion_ventas

print('* Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes *\n')

salir = False
while not salir:
    print('''Menú Principal:
1. Gestión de Clientes
2. Gestión de Destinos
3. Gestión de Ventas
4. Botón de Arrepentimiento
5. Salir''')

    opcion = input('Selecciona una opción: ')

    if opcion == '1':
        print('\nGestión de Clientes:')
        print('''1. Agregar Cliente
2. Listar Clientes
3. Modificar Cliente
4. Eliminar Cliente
5. Volver al menú principal''')

        subopcion = input('Seleccione una opción: ')

        if subopcion == '1':
            gestion_clientes.agregar_cliente()
        elif subopcion == '2':
            gestion_clientes.listar_clientes()
        elif subopcion == '3':
            gestion_clientes.modificar_cliente()
        elif subopcion == '4':
            gestion_clientes.eliminar_cliente()

    elif opcion == '2':
        print('\nGestión de Destinos:')
        print('''1. Agregar Destino
2. Listar Destinos
3. Modificar Destino
4. Eliminar Destino
5. Volver al menú principal''')

        subopcion_destino = input("Seleccione una opción: ")

        if subopcion_destino == '1':
            gestion_destinos.agregar_destino()
        elif subopcion_destino == '2':
            gestion_destinos.listar_destinos()
        elif subopcion_destino == '3':
            gestion_destinos.modificar_destino()
        elif subopcion_destino == '4':
            gestion_destinos.eliminar_destino()

    elif opcion == '3':
        print('\nGestión de Ventas:')
        print('''1. Registrar Venta
2. Listar Ventas
3. Modificar Estado de Venta
4. Volver al menú principal''')

        venta_op = input('Seleccione una opción: ')

        if venta_op == '1':
            gestion_ventas.registrar_venta()
        elif venta_op == '2':
            gestion_ventas.listar_ventas()
        elif venta_op == '3':
            gestion_ventas.modificar_estado_venta()

    elif opcion == '4':
        print("\nActivando Botón de Arrepentimiento...")
        gestion_ventas.anular_venta_reciente()

    elif opcion == '5':
        print('Gracias por usar SkyRoute. ¡Hasta luego!\n')
        salir = True

    else:
        print('Opción inválida. Intente de nuevo.\n')
