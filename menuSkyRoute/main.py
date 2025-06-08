import gestion_clientes
import gestion_destinos
import gestion_ventas

def menu_clientes():
    while True:
        print('\nGestión de Clientes:')
        print('''1. Agregar Cliente
2. Listar Clientes
3. Modificar Cliente
4. Eliminar Cliente
5. Volver al menú principal''')

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            gestion_clientes.agregar_cliente()
        elif opcion == '2':
            gestion_clientes.listar_clientes()
        elif opcion == '3':
            gestion_clientes.modificar_cliente()
        elif opcion == '4':
            gestion_clientes.eliminar_cliente()
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def menu_destinos():
    while True:
        print('\nGestión de Destinos:')
        print('''1. Agregar Destino
2. Listar Destinos
3. Modificar Destino
4. Eliminar Destino
5. Volver al menú principal''')

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestion_destinos.agregar_destino()
        elif opcion == '2':
            gestion_destinos.listar_destinos()
        elif opcion == '3':
            gestion_destinos.modificar_destino()
        elif opcion == '4':
            gestion_destinos.eliminar_destino()
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def menu_ventas():
    while True:
        print('\nGestión de Ventas:')
        print('''1. Registrar Venta
2. Listar Ventas
3. Modificar Estado de Venta
4. Volver al menú principal''')

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            gestion_ventas.registrar_venta()
        elif opcion == '2':
            gestion_ventas.listar_ventas()
        elif opcion == '3':
            gestion_ventas.modificar_estado_venta()
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Programa principal
def main():
    print('* Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes *\n')

    while True:
        print('''Menú Principal:
1. Gestión de Clientes
2. Gestión de Destinos
3. Gestión de Ventas
4. Botón de Arrepentimiento
5. Salir''')

        opcion = input('Selecciona una opción: ')

        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_destinos()
        elif opcion == '3':
            menu_ventas()
        elif opcion == '4':
            gestion_ventas.anular_venta_reciente()
        elif opcion == '5':
            print('Gracias por usar SkyRoute. ¡Hasta luego!\n')
            break
        else:
            print('Opción inválida. Intente de nuevo.\n')

if __name__ == "__main__":
    main()
