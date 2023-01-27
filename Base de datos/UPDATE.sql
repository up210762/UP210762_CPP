/* 
	DEFINICION CRUD  

	C - CREATE -> INSERT
	R - READ -> SELECT
	U - UPDATE -> UPDATE
	D - DELETE -> DELETE
*/

-- UPDATE

UPDATE FirstDataBase.JugadorSinRelaciones
SET Descripcion = 'NeCeSita PracTICar +'

/*
-- UPDATE + CONDITIONAL + FUNCTION
UPDATE FirstDataBase.JugadorSinRelaciones
SET Estatura = 1.70
WHERE Id IN(3,4)




UPDATE FirstDataBase.JugadorSinRelaciones
SET Deleted = 0

UPDATE FirstDataBase.JugadorSinRelaciones
SET Deleted = 1
WHERE Estatura is null
*/

/* Select all information */
