ALTER TABLE JugadorSinRelaciones
ADD (`NumeroCamiseta` nvarchar(200) NULL,
	`Descripcion` nvarchar(10000) NULL,
    `Estatura` decimal(18,2) NULL,
    `FechaRegistro` datetime NULL
    )