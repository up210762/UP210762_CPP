-- Tabla de proceso
SELECT * FROM `Proyecto2_iscdb`.`JugadorConRelaciones`;


-- Tablas de catalogos
SELECT * FROM `Proyecto2_iscdb`.`PocisionId`;
SELECT * FROM `Proyecto2_iscdb`.`EquipoId`;
SELECT * FROM `Proyecto2_iscdb`.`NacionalidadId`;

-- CREAR PRIMERA NACIONALIDAD
INSERT INTO `Proyecto2_iscdb`.`NacionalidadId` VALUES
(1, 'MEXICANA', 1, 0);

INSERT INTO `Proyecto2_iscdb`.`PocisionId` VALUES
(1, 'Portero', 1, 0);

INSERT INTO `Proyecto2_iscdb`.`EquipoId` VALUES
(1, 'Juventus', 'Allegri', 1, 0);

Insert into `Proyecto2_iscdb`.`JugadorConRelaciones` values
(3, 'Del Piero 3',1,1,3, curdate(),1,1.80,curdate());

-- Join Equipo
SELECT * 
FROM `Proyecto2_iscdb`.`JugadorConRelaciones` 
INNER JOIN `Proyecto2_iscdb`.`EquipoId`;

SELECT *
FROM Proyecto2_iscdb.JugadorConRelaciones AS JCR INNER JOIN
	Proyecto2_iscdb.EquipoId E ON JCR.EquipoId = E.Id;

-- Join Equipo - Columnas específicas
SELECT JCR.*, E.*
FROM `Proyecto2_iscdb`.`JugadorConRelaciones` JCR INNER JOIN
	`Proyecto2_iscdb`. `EquipoId` E ON JCR.EquipoId = E.Id;
    
-- Join Equipo - Columnas específicas
SELECT JCR.Nombre, E.Nombre
FROM `Proyecto2_iscdb`.`JugadorConRelaciones` JCR INNER JOIN
	`Proyecto2_iscdb`. `EquipoId` E ON JCR.EquipoId = E.Id;

SELECT *
FROM `Proyecto2_iscdb`.`JugadorConRelaciones` as JCR inner join
	`Proyecto2_iscdb`.`EquipoId` as E ON E.Id inner join
    `Proyecto2_iscdb`.`NacionalidadId` as N ON N.Id inner join
    `Proyecto2_iscdb`.`PocisionId` as P ON P.Id = JCR.NacionalidadId;
    
