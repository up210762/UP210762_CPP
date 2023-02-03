/* 
	DEFINICION CRUD  

	C - CREATE -> INSERT
	R - READ -> SELECT
	U - UPDATE -> UPDATE
	D - DELETE -> DELETE
*/

-- GENERAL INSERT

/*
INSERT INTO FirstDataBase.JugadorSinRelaciones	
    (Id, Name, NumeroCamiseta)
	VALUES
	(4, 'Lalo' , '15'),
	(4, 'Lalo' , '15'),
	(4, 'Lalo' , '15'),
	(4, 'Lalo' , '15'),
	(4, 'Lalo' , '15'),
	(4, 'Lalo' , '15'),
	(4, 'Lalo' , '15'),
	(4, 'Lalo' , '15'),
	(4, 'Lalo' , '15'),
	(4, 'Lalo' , '15')
*/

INSERT INTO FirstDataBase.JugadorSinRelaciones
	(Id, Name, Posicion, Equipo, FechaNacimiento, Nacionalidad, NumeroCamiseta, Descripcion, Estatura, FechaRegistro)
	VALUES
	(1, 'Jugador_1','P_1','Necaxa','1900-01-01','Mexicana',1 , '', ROUND(RAND() = 10,10), NULL),
    (2, 'Jugador_1','P_2','Necaxa','1900-01-01','Mexicana',2 , '', ROUND(RAND() = 10,10), NULL)