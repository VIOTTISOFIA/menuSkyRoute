-- Crear base de datos evidencia3
CREATE DATABASE IF NOT EXISTS evidencia3;
USE evidencia3;

-- Tabla Cliente
CREATE TABLE Cliente (
    ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    Razon_Social VARCHAR(100),
    CUIT VARCHAR(20),
    Correo VARCHAR(100)
);

-- Tabla Destino
CREATE TABLE Destino (
    ID_Destino INT AUTO_INCREMENT PRIMARY KEY,
    Ciudad VARCHAR(100),
    Pais VARCHAR(100),
    Costo_base DECIMAL(10, 2)
);

-- Tabla Estado_Venta
CREATE TABLE Estado_Venta (
    ID_Estado_Venta INT AUTO_INCREMENT PRIMARY KEY,
    Tipo_estado VARCHAR(50)
);

-- Tabla Venta
CREATE TABLE Venta (
    ID_Venta INT AUTO_INCREMENT PRIMARY KEY,
    ID_Cliente INT,
    ID_Destino INT,
    Fecha_venta DATE,
    Costo_total DECIMAL(10, 2),
    ID_Estado_Venta INT,
    Fecha_anulacion DATE,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
    FOREIGN KEY (ID_Destino) REFERENCES Destino(ID_Destino),
    FOREIGN KEY (ID_Estado_Venta) REFERENCES Estado_Venta(ID_Estado_Venta)
);
-- Clientes
INSERT INTO Cliente (Razon_Social, CUIT, Correo)
VALUES 
('Gonella S.A.', '20-36143931-3', 'lgonella@email.com'),
('Gagliardi S.R.L.', '27-37618201-7', 'lgagliardi@email.com'),
('Leimgruber y Cía.', '23-27361689-1', 'gleimgruber@email.com'),
('Nadales Group', '25-37128034-2', 'knadales@email.com'),
('Viotti Servicios', '20-35822944-4', 'sviotti@email.com');

-- Destinos
INSERT INTO Destino (Ciudad, Pais, Costo_base)
VALUES 
('París', 'Francia', 1200.00),
('Berlín', 'Alemania', 1100.00),
('Oslo', 'Noruega', 1300.00),
('Copenhague', 'Dinamarca', 1250.00),
('Estocolmo', 'Suecia', 1280.00);

-- Estados de Venta
INSERT INTO Estado_Venta (Tipo_estado)
VALUES 
('Confirmada'),
('Pendiente'),
('Cancelada');

-- Ventas (usando IDs asumidos según orden de inserción)
INSERT INTO Venta (ID_Cliente, ID_Destino, Fecha_venta, Costo_total, ID_Estado_Venta, Fecha_anulacion)
VALUES 
(1, 1, '2025-04-01', 1200.00, 1, NULL),
(2, 2, '2025-04-03', 1100.00, 2, NULL),
(3, 3, '2025-04-05', 1300.00, 1, NULL),
(4, 4, '2025-04-07', 1250.00, 3, '2025-04-08'),
(5, 5, '2025-04-10', 1280.00, 1, NULL);

SELECT * FROM cliente  ORDER BY razon_social  ASC;
SELECT * FROM venta WHERE fecha_venta = '2025-04-03';

-- actualice la tabla de ventas por que solo habia una venta por cliente 
-- Ventas variadas por cliente
INSERT INTO Venta (ID_Cliente, ID_Destino, Fecha_venta, Costo_total, ID_Estado_Venta, Fecha_anulacion)
VALUES 
-- Gonella Lucas (Cliente 1)
(1, 1, '2025-04-01', 1200.00, 1, NULL),
(1, 3, '2025-05-15', 1350.00, 2, NULL),

-- Gagliardi Luciana (Cliente 2)
(2, 2, '2025-04-03', 1100.00, 2, NULL),
(2, 4, '2025-05-20', 1250.00, 3, '2025-05-22'),

-- Leimgruber Guillermo (Cliente 3)
(3, 3, '2025-04-05', 1300.00, 1, NULL),
(3, 1, '2025-05-12', 1190.00, 1, NULL),

-- Nadales Katya María (Cliente 4)
(4, 4, '2025-04-07', 1250.00, 3, '2025-04-08'),
(4, 5, '2025-05-01', 1280.00, 1, NULL),

-- Viotti Sofia Anahí (Cliente 5)
(5, 5, '2025-04-10', 1280.00, 1, NULL),
(5, 2, '2025-05-18', 1120.00, 2, NULL);

-- para obtener la ultima venta de cada cliente tenemos que usar funCiones combinadas MAX(fecha_venta) y GROUP BY uno tabla cliente y venta. Luego agrupo por cliente y razon social.

SELECT 
    c.ID_Cliente,
    c.Razon_Social,
    MAX(v.Fecha_venta) AS Ultima_Fecha_Venta
FROM 
    Cliente c
JOIN 
    Venta v ON c.ID_Cliente = v.ID_Cliente
GROUP BY 
    c.ID_Cliente, c.Razon_Social;
    
-- agregue un pais mas con S 
INSERT INTO Destino (Ciudad, Pais, Costo_base)
VALUES ('Zúrich', 'Suiza', 1150.00);

-- listar los paises que comienzan con S, utilizamos like "s%" que significa empieza con S y cualquier cosa despues. 
SELECT * FROM Destino
WHERE Pais LIKE 'S%';

-- cuantas ventas se realizaron por pais ? join une cada venta con su destino para saber el pais, GROUP BY d.pais agrupa las ventas segun el pais destino 
-- COUNT( v.ID_ventas) cuenta cuantas ventas se hicieron por pais.
SELECT 
    d.Pais,
    COUNT(v.ID_Venta) AS Cantidad_Ventas
FROM 
    Venta v
JOIN 
    Destino d ON v.ID_Destino = d.ID_Destino
GROUP BY 
    d.Pais;

SELECT c.ID_Cliente, c.Razon_Social, COUNT(v.ID_Venta) AS Cantidad_Ventas
FROM Cliente c
JOIN Venta v ON c.ID_Cliente = v.ID_Cliente
GROUP BY c.ID_Cliente, c.Razon_Social
ORDER BY Cantidad_Ventas DESC
LIMIT 1;    