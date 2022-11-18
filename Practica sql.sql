USE Prueba;

/* Consulta de el Aeropuerto con mas movimiento  */
WITH Aeropm as(
SELECT *, ROW_NUMBER() OVER (PARTITION BY v.ID_AEROPUERTO ORDER BY v.ID_AEROPUERTO DESC) as num
FROM Vuelos as v
WHERE ID_AEROPUERTO in(
	SELECT ID_AEROPUERTO
	FROM Vuelos
	GROUP BY ID_AEROPUERTO
	HAVING COUNT(*)>1
)
)

SELECT TOP 1 Aeropuertos.NOMBRE_AEROLINEA
FROM Aeropm
INNER JOIN Aeropuertos
ON Aeropm.ID_AEROPUERTO = Aeropuertos.ID_AEROPUERTO
WHERE num =(SELECT MAX(num) FROM Aeropm);



/* Consulta de el Aerolinea con mas movimiento  */
WITH Aeropm2 as(
SELECT *, ROW_NUMBER() OVER (PARTITION BY v.ID_AEROLINEA ORDER BY v.ID_AEROLINEA DESC) as num
FROM Vuelos as v
WHERE ID_AEROLINEA in(
	SELECT ID_AEROLINEA
	FROM Vuelos
	GROUP BY ID_AEROLINEA
	HAVING COUNT(*)>1
)
)


SELECT TOP 1 Aerolineas.NOMBRE_AEROLINEA
FROM Aeropm2
INNER JOIN Aerolineas
ON Aeropm2.ID_AEROLINEA = Aerolineas.ID_AEROLINEA
WHERE num =(SELECT MAX(num) FROM Aeropm2);



/* Consulta el dia con mas movimientos  */

WITH DIAs as(
SELECT *, ROW_NUMBER() OVER (PARTITION BY v.DIA ORDER BY v.DIA DESC) as num
FROM Vuelos as v
WHERE DIA in(
	SELECT DIA
	FROM Vuelos
	GROUP BY DIA
	HAVING COUNT(*)>1
)
)
SELECT TOP 1 Dias.DIA
FROM DIAs
WHERE num =(SELECT MAX(num) FROM DIAs);