# Sistema de Gestión de Pasajes - SkyRoute
print('* Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes *\n')

# Variables para almacenar los datos del cliente
cliente_cuit = None
cliente_nombre = None
cliente_correo = None

# Variables para almacenar el destino y su costo
destino_nombre = None
destino_costo = None
destino_ciudad = None

salir = False
while not salir:
    print('''Menú Principal:
1. Cliente
2. Destino de Viaje
3. Ventas de Pasajes
4. Políticas
5. Salir''')

    opcion = input('Selecciona una opción: ')

    if opcion == '1':
        print('\nGestión de Cliente:')
        print('''1. Ver Cliente
2. Agregar Cliente
3. Modificar Cliente
4. Eliminar Cliente
5. Volver al menú principal''')

        subopcion = input('Seleccione una opción: ')

        if subopcion == '1':
            print("\nListado de clientes:")
            print("------------------------------")
            if cliente_cuit is not None:
                print(f"CUIT: {cliente_cuit}")
                print(f"Nombre/Razón Social: {cliente_nombre}")
                print(f"Correo: {cliente_correo}")
                print("------------------------------\n")
            else:
                print("No hay cliente registrado.\n")

        elif subopcion == '2':
            print("\nAgregar Cliente:")
            cliente_cuit = input('CUIT del cliente: ')
            cliente_nombre = input('Nombre/Razón Social del cliente: ')
            cliente_correo = input('Correo del cliente: ')
            print('Cliente guardado correctamente.\n')

        elif subopcion == '3':
            if cliente_cuit is not None:
                cuit_ingresado = input('Ingrese el CUIT del cliente a modificar: ')
                if cuit_ingresado == cliente_cuit:
                    print("\nDatos actuales del cliente:")
                    print("------------------------------")
                    print(f"CUIT: {cliente_cuit}")
                    print(f"Nombre/Razón Social: {cliente_nombre}")
                    print(f"Correo: {cliente_correo}")
                    print("------------------------------\n")

                    print('1. Modificar Nombre/Razón Social\n2. Modificar Correo')
                    campo = input('Seleccione campo a modificar: ')
                    if campo == '1':
                        cliente_nombre = input('Nuevo nombre/Razón Social: ')
                        print('Nombre actualizado.\n')
                    elif campo == '2':
                        cliente_correo = input('Nuevo correo: ')
                        print('Correo actualizado.\n')
                    else:
                        print('Opción inválida.\n')
                else:
                    print('CUIT no encontrado. No se puede modificar.\n')
            else:
                print('No hay cliente registrado.\n')

        elif subopcion == '4':
            if cliente_cuit is not None:
                cuit_ingresado = input('Ingrese el CUIT del cliente a eliminar: ')
                if cuit_ingresado == cliente_cuit:
                    print("\nCliente eliminado:")
                    print("------------------------------")
                    print(f"Nombre/Razón Social: {cliente_nombre}")
                    print(f"Correo: {cliente_correo}")
                    print(f"CUIT: {cliente_cuit}")
                    print("------------------------------\n")

                    cliente_cuit = None
                    cliente_nombre = None
                    cliente_correo = None
                else:
                    print('CUIT no encontrado. No se puede eliminar.\n')
            else:
                print('No hay cliente para eliminar.\n')

    elif opcion == '2':
        print('\nGestión de Destinos:')
        print('''1. Ver Destino
2. Agregar Destino
3. Modificar Destino
4. Eliminar Destino''')

        subopcion_destino = input("Seleccione una opción: ")

        if subopcion_destino == '1':
            if destino_nombre is not None:
                print("\nDestino actual:")
                print("------------------------------")
                print(f"Destino: {destino_nombre}")
                print(f"Ciudad: {destino_ciudad}")
                print(f"Costo: ${destino_costo}")
                print("------------------------------\n")
            else:
                print("No hay destino registrado.\n")

        elif subopcion_destino == '2':
            destino_nombre = input("Nombre del destino: ")
            destino_ciudad = input("Nombre de la ciudad: ")
            destino_costo = input("Costo del viaje: ")
            print("\nDestino guardado correctamente.\n")

        elif subopcion_destino == '3':
            if destino_nombre is not None:
                print("\nDatos actuales del destino:")
                print("------------------------------")
                print(f"Destino: {destino_nombre}")
                print(f"Ciudad: {destino_ciudad}")
                print(f"Costo: ${destino_costo}")
                print("------------------------------")
                destino_nombre = input("Nuevo nombre del destino: ")
                destino_ciudad = input("Nuevo nombre de la ciudad: ")
                destino_costo = input("Nuevo costo del viaje: ")
                print("------------------------------")
                print("Destino actualizado correctamente.\n")
            else:
                print("No hay destino registrado para modificar.\n")

        elif subopcion_destino == '4':
            if destino_nombre is not None:
                nombre_ingresado = input("Ingrese el nombre del destino a eliminar: ")
                if nombre_ingresado == destino_nombre:
                    print("\nDestino eliminado:")
                    print("------------------------------")
                    print(f"Nombre: {destino_nombre}")
                    print(f"Ciudad: {destino_ciudad}")
                    print(f"Costo: {destino_costo}")
                    print("------------------------------\n")
                
                    destino_nombre = None
                    estino_ciudad = None
                    destino_costo = None
                else:
                    print("Nombre de destino no encontrado. No se puede eliminar.\n")
            else:
                print("No hay destino registrado para eliminar.\n")

    elif opcion == '3':
        print('\nVentas de Pasajes:')
        print('1. Ver todas las ventas\n2. Ventas por cliente\n3. Ventas recientes\n4. Volver')
        venta_op = input('Selecciona una opción: ')

        if venta_op == '1':
            print('Mostrando todas las ventas...\n')
        elif venta_op == '2':
            cuit_busqueda = input('Ingrese el CUIT del cliente: ')
            if cuit_busqueda == cliente_cuit:
                print(f'Mostrando ventas de cliente con CUIT {cuit_busqueda}...\n')
            else:
                print('CUIT no encontrado. No hay ventas registradas para este cliente.\n')
        elif venta_op == '3':
            print('Mostrando ventas de la última semana...\n')
        elif venta_op == '4':
            print('Volviendo al menú principal...\n')

    elif opcion == '4':
        print('''\nPolíticas de SkyRoute:
- Pasajes personales e intransferibles.
- Cambios con 48hs de anticipación.
- Botón de Arrepentimiento disponible.

¿Cancelar compra?
1. Sí
2. No''')
        decision = input('Selecciona una opción: ')
        if decision == '1':
            print('Compra cancelada exitosamente.\n')
        elif decision == '2':
            print('Volviendo al menú principal...\n')

    elif opcion == '5':
        print('Gracias por usar SkyRoute. ¡Hasta luego!\n')
        salir = True

    else:
        print('Opción inválida. Intente de nuevo.\n')