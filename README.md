### SkyRoute - Sistema de Gestión de Pasajes

Este proyecto implementa un sistema básico de gestión para una agencia de pasajes de avion, 
facilitando la administración de clientes, destinos y ventas. 
Está diseñado para interactuar con una base de datos MySQL y proporciona una interfaz de consola.

## Características

El sistema opera modularmente, cada modulo con su funcionalida especifica,
permitiendo su modifiacion y reutilizacion.

## Gestión de Clientes

 - Agregar Cliente: Permite registrar nuevos clientes con su razón social, CUIT y correo electrónico.
 - Listar Clientes: Muestra un listado completo de todos los clientes registrados.
 - Modificar Cliente: Facilita la actualización de la información de un cliente existente.
 - Eliminar Cliente: Permite dar de baja a un cliente del sistema.
   
## Gestión de Destinos

 - Agregar Destino: Permite registrar nuevos destinos con su ciudad, país y costo base.
 - Listar Destinos: Muestra un listado de todos los destinos disponibles.
 - Modificar Destino: Facilita la actualización de la información de un destino.
 - Eliminar Destino: Permite eliminar un destino del sistema.
   
## Gestión de Ventas

 - Registrar Venta: Permite registrar una nueva venta. Las ventas se registran inicialmente como "Pendientes".
 - Listar Ventas: Muestra un listado detallado de todas las ventas, incluyendo su estado y, si aplica, la fecha de anulación.
 - Modificar Estado de Venta: Permite cambiar el estado de una venta (Confirmada, Pendiente, Cancelada).
 - Botón de Arrepentimiento: Una funcionalidad específica para anular la venta "Pendiente" más reciente, registrando la fecha de anulación automáticamente.


### Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

main.py: Es el punto de entrada principal del sistema. Ofrece un menú interactivo en la consola.
gestion_clientes.py: Contiene las funciones para realizar operaciones CRUD sobre la tabla de clientes en la base de datos.
gestion_destinos.py: Contiene las funciones para realizar operaciones CRUD sobre la tabla de destinos en la base de datos.
gestion_ventas.py: Contiene las funciones para registrar, listar y modificar el estado de las ventas, incluyendo la lógica para el "botón de arrepentimiento".
conexion_base_datos.py: Módulo que encapsula las funciones para establecer (conectar()) y cerrar (cerrar_conexion()) la conexión con la base de datos MySQL.

## Requisitos

Python 3.x
mysql.connector: La librería para interactuar con bases de datos MySQL.
Puedes instalarla desde la terminal: pip install mysql-connector-python

Acceso a la Base de datos de SkyRoute o al codigo para crearla. Se encuentra un archivo para tal caso a modo
de prueba. Archivo baseDatos.sql

## Documentacion adicional

Se adjunta dos ducmentos:
-Etica y ejercicio profecional Evidencia 2
-Etica y ejercicio profecional Evidencai 3

Se ha tenido en cuenta la legislación de derechos de autor sobre software, asegurando que este código es para fines demostrativos y educativos, 
respetando las licencias aplicables si se integrara con otros componentes.

En cuanto a la seguridad y datos del cliente, este sistema maneja información sensible como la razón social, CUIT y correo electrónico.
Se recomienda implementar medidas de seguridad adicionales en un entorno de producción, tales como:

Validación de entradas: Para prevenir inyecciones SQL y otros ataques.
Manejo de errores: Implementar bloques try-except para gestionar excepciones de la base de datos y otras operaciones.
Auditoría y logs: Registrar las operaciones importantes para fines de seguridad y seguimiento.
Autenticación y autorización: Los usuarios deberían autenticarse y tener permisos específicos para acceder a ciertas funcionalidades.
Cifrado de datos: Especialmente para datos sensibles almacenados o transmitidos.
