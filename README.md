# SkyRoute - Sistema de Gestión de Pasajes

Este proyecto implementa un sistema básico de gestión para una agencia de pasajes de avion, 
facilitando la administración de clientes, destinos y ventas. 
Está diseñado para interactuar con una base de datos MySQL y proporciona una interfaz de consola.

Además del presente archivo README, se van a encontrar con las carpetas:

- Manu SkyRoute: Código python de gestión de ventas y clientes.
- ABP: Documentación, video y póster del mismo.
- Base de datos: Esquema DER y código sql
- Etica y deontologia: Documentación para orientar la práctica de desarrollo de software y base de datos en su marco ético y legal.

## Características

El sistema opera modularmente, cada modulo con su funcionalida especifica,
permitiendo su modifiacion y reutilizacion.

### Gestión de Clientes

 - Agregar Cliente: Permite registrar nuevos clientes con su razón social, CUIT y correo electrónico.
 - Listar Clientes: Muestra un listado completo de todos los clientes registrados.
 - Modificar Cliente: Facilita la actualización de la información de un cliente existente.
 - Eliminar Cliente: Permite dar de baja a un cliente del sistema.
   
### Gestión de Destinos

 - Agregar Destino: Permite registrar nuevos destinos con su ciudad, país y costo base.
 - Listar Destinos: Muestra un listado de todos los destinos disponibles.
 - Modificar Destino: Facilita la actualización de la información de un destino.
 - Eliminar Destino: Permite eliminar un destino del sistema.
   
### Gestión de Ventas

 - Registrar Venta: Permite registrar una nueva venta. Las ventas se registran inicialmente como "Pendientes".
 - Listar Ventas: Muestra un listado detallado de todas las ventas, incluyendo su estado y, si aplica, la fecha de anulación.
 - Modificar Estado de Venta: Permite cambiar el estado de una venta (Confirmada, Pendiente, Cancelada).
 - Botón de Arrepentimiento: Una funcionalidad específica para anular la venta "Pendiente" más reciente, registrando la fecha de anulación automáticamente.


## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

main.py: Es el punto de entrada principal del sistema. Ofrece un menú interactivo en la consola.
gestion_clientes.py: Contiene las funciones para realizar operaciones CRUD sobre la tabla de clientes en la base de datos.
gestion_destinos.py: Contiene las funciones para realizar operaciones CRUD sobre la tabla de destinos en la base de datos.
gestion_ventas.py: Contiene las funciones para registrar, listar y modificar el estado de las ventas, incluyendo la lógica para el "botón de arrepentimiento".
conexion_base_datos.py: Módulo que encapsula las funciones para establecer (conectar()) y cerrar (cerrar_conexion()) la conexión con la base de datos MySQL.
Gestion de Codigo y Control de Versiones. Para facilitar la colaboracion y el seguimiento de cambio, el proyecto se gestiona utilizando Git y GitHub. Esto permite: Trabajo colaborativo. Historial y Reversion de cambios: En caso de errores, es posible volver a versiones anteriores del codigo.

## Requisitos

Python 3.x
mysql.connector: La librería para interactuar con bases de datos MySQL.
Puedes instalarla desde la terminal: pip install mysql-connector-python

Acceso a la Base de datos de SkyRoute o al codigo para crearla. Se encuentra un archivo para tal caso a modo
de prueba. Archivo baseDatos.sql

## Documentacion adicional

### Se adjunta dos ducumentos en la carpeta Etica y deontologia
-Etica y ejercicio profecional Evidencia 2
-Etica y ejercicio profecional Evidencia 3

Se ha tenido en cuenta la legislación de derechos de autor sobre software, asegurando que este código es para fines demostrativos y educativos, 
respetando las licencias aplicables si se integrara con otros componentes.

### En la carpeta Base de datos:

* Archivo contiene el Diagrama de Entidad-Relación (DER) de la base de datos de SkyRoute. El DER es una representación visual de la estructura de la base de datos, mostrando:

Las entidades principales (ej., Cliente, Destino, Venta, Estado_Venta).
Los atributos de cada entidad (ej., Razon_Social, Costo_base, Fecha_venta).
Las relaciones entre las entidades (ej., un cliente puede tener muchas ventas, una venta tiene un destino).
Las claves primarias y foráneas que definen estas relaciones y aseguran la integridad referencial.


*Archivo SQL que ejemplifica el uso de:

 DDL: Contiene las sentencias SQL necesarias para crear la estructura de la base de datos, incluyendo:
CREATE DATABASE: Para crear la base de datos skyroute.
CREATE TABLE: Para definir la estructura de cada tabla (cliente, destino, venta, estado_venta), sus columnas, tipos de datos, restricciones (NOT NULL, UNIQUE) y la definición de claves primarias y foráneas.


DML: Incluye sentencias SQL para interactuar con los datos dentro de las tablas existentes, como:
INSERT INTO: Para añadir registros de ejemplo en las tablas (clientes, destinos, estados de venta y ventas).
SELECT: Para consultar y recuperar datos de las tablas.
UPDATE: Para modificar registros existentes.
DELETE: Para eliminar registros de las tablas.

En cuanto a la seguridad y datos del cliente, este sistema maneja información sensible como la razón social, CUIT y correo electrónico.
Se recomienda implementar medidas de seguridad adicionales en un entorno de producción, tales como:

Validación de entradas: Para prevenir inyecciones SQL y otros ataques.
Manejo de errores: Implementar bloques try-except para gestionar excepciones de la base de datos y otras operaciones.
Auditoría y logs: Registrar las operaciones importantes para fines de seguridad y seguimiento.
Autenticación y autorización: Los usuarios deberían autenticarse y tener permisos específicos para acceder a ciertas funcionalidades.

## Carpeta ABP

- Documento de presentación del ABP
- Video de presentación del equipo de trabajo.
- Póster del proyecto
- 

#### SkyRoute - Sistema de Gestión de Pasajes
#### Desarrollado por: GRUPO 2 S.A.S.
#### Proyecto educativo - Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial
#### Módulo: Programador | Año: 2025
#### Sistema básico para la gestión de pasajes aéreos, clientes, destinos y ventas.
#### Parte del código fue desarrollado con asistencia de la herramienta ChatGPT (OpenAI),y adaptado por el equipo para cumplir con los objetivos del proyecto.
#### Todos los derechos reservados bajo Ley 11.723 (Propiedad Intelectual - Argentina).
#### Prohibida su reproducción o distribución total o parcial sin autorización de los autores.
