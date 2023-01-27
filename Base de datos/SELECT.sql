/*
   ESTE ES UN GRAN COMENTARIO
*/

-- ESTE ES UN PEQUEÑO COMENTARIO

/* 
	DEFINICION CRUD  

	C - CREATE -> INSERT
	R - READ -> SELECT
	U - UPDATE -> UPDATE
	D - DELETE -> DELETE
*/


/* SELECT ALL INFORMATION */
SELECT * FROM FirstDataBase.JugadorSinRelaciones

-- SELECT SPECIFIC INFORMATION

SELECT Name, Equipo, Estatura
FROM `FirstDataBase`.`JugadorSinRelaciones`

-- SELECT SPECIFIC INFORMATION WITH ALIAS 
SELECT Name As Nombre, Equipo, Estatura
FROM `FirstDataBase`.`JugadorSinRelaciones`

-- SELECT COUNT ROWS
SELECT COUNT(*) AS NumeroJugadores FROM [dbo].[JugadorSinRelaciones]

-- SELECT + CONDITIONALS
SELECT COUNT(*) as CamisetasRepetidas FROM [dbo].[JugadorSinRelaciones]
WHERE NumeroCamiseta = '15'

-- SELECT + CONDITIONAL + FUCNTION[BETWEEN]

SELECT * FROM [dbo].[JugadorSinRelaciones]
WHERE Estatura between 1.70 and 1.75

-- SELECT + CONDITIONAL + FUCNTION[BETWEEN] + GROUP BY -- Pendiente

SELECT Count(*) AS JugadoresEstaturas, Estatura FROM [dbo].[JugadorSinRelaciones]
WHERE Estatura between 1.70 and 1.76
Group by Estatura


-- SELECT + FUNCTION UPPER/LOWER
SELECT Name, LOWER(Descripcion)
 FROM [dbo].[JugadorSinRelaciones]

 SELECT Name, UPPER(Descripcion)
 FROM [dbo].[JugadorSinRelaciones]
 
 -- SELECT + FUNCTION REPLACE
 SELECT REPLACE( Descripcion, '+', 'más')
 FROM [dbo].[JugadorSinRelacion]
 
 -- SELECT + FUNCTION CASE_WHEN Evaluando cantidad de registros
 SELECT
 CASE 
	WHEN COUNT(Descripcion) > 4 THEN ' Tenemos más de 4 valores'
	WHEN COUNT(Descripcion) < 4 THEN ' Tenemos menos de 4 valores'
    WHEN COUNT(Descripcion) = 4 THEN ' Tenemos justo 4 valores'
 ELSE 'Estamos vacios' END as 'Desc_Columnas'
 FROM [dbo].[JugadorSinRelaciones]
 
 select COUNT(Descripcion)
	FROM [dbo].[JugadorSinRelaciones]
    
-- SELECT + FUNCTION ISNULL

select ISNULL(Descripcion, 'yo vengo vacio')
	FROM dbo.JugadorSinRelaciones

SELECT
CASE
	WHEN Descripcion = null THEN 'To vengo vacio'
    ELSE Descripcion END
FROM dbo.JugadorSinRelaciones
