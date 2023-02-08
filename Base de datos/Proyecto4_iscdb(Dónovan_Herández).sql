 -- Creación de las tablas

CREATE TABLE `BoletosPerdidos` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `TotalBoletos` int NOT NULL,
  `BoletosNoDevueltos` int NOT NULL,
  `Periodo` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `Periodo_FK` (`Periodo`),
  KEY `TotalBoletos_FK` (`TotalBoletos`),
  KEY `BoletosPerdidos_FK` (`BoletosNoDevueltos`),
  CONSTRAINT `BoletosPerdidos_FK` FOREIGN KEY (`BoletosNoDevueltos`) REFERENCES `TransaccionesCarros` (`IdTC`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Periodo_FK` FOREIGN KEY (`Periodo`) REFERENCES `Parametros` (`IdP`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `TotalBoletos_FK` FOREIGN KEY (`TotalBoletos`) REFERENCES `EntradasSalidas` (`IdE&S`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `EntradasSalidas` (
  `IdE&S` int NOT NULL AUTO_INCREMENT,
  `TotalEntradas` int NOT NULL,
  `TotalSalidas` int NOT NULL,
  PRIMARY KEY (`IdE&S`),
  KEY `EntradasSalidas_FK_1` (`TotalSalidas`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Parametros` (
  `IdP` int NOT NULL AUTO_INCREMENT,
  `PeriodoTotal` varchar(200) NOT NULL,
  PRIMARY KEY (`IdP`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `TransaccionesCarros` (
  `IdTC` int NOT NULL AUTO_INCREMENT,
  `TotalTransacciones` int NOT NULL,
  PRIMARY KEY (`IdTC`),
  KEY `TransaccionesCarros_FK` (`TotalTransacciones`),
  CONSTRAINT `TransaccionesCarros_FK` FOREIGN KEY (`TotalTransacciones`) REFERENCES `EntradasSalidas` (`IdE&S`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




-- Llaves foráneas

ALTER TABLE Proyecto4_iscdb.BoletosPerdidos 
ADD CONSTRAINT TotalBoletos_FK
FOREIGN KEY (TotalBoletos) 
REFERENCES Proyecto4_iscdb.EntradasSalidas(`IdE&S`) 
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Proyecto4_iscdb.BoletosPerdidos 
ADD CONSTRAINT Periodo_FK
FOREIGN KEY (Periodo) 
REFERENCES Proyecto4_iscdb.Parametros(IdP) 
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Proyecto4_iscdb.BoletosPerdidos 
ADD CONSTRAINT BoletosPerdidos_FK 
FOREIGN KEY (BoletosNoDevueltos) 
REFERENCES Proyecto4_iscdb.TransaccionesCarros(IdTC) 
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Proyecto4_iscdb.TransaccionesCarros 
ADD CONSTRAINT TransaccionesCarros_FK 
FOREIGN KEY (IdTC) 
REFERENCES Proyecto4_iscdb.BoletosPerdidos(Id);



-- Scrips to insert values inside of tables

INSERT INTO `Proyecto4_iscdb`.`Parametros` 
(PeriodoTotal)
VALUES
	('DIARIO'),
	('SEMANAL'),
	('MENSUAL'),
	('ANUAL');

INSERT INTO Proyecto4_iscdb.EntradasSalidas 
(TotalEntradas, TotalSalidas)
VALUES
(34, 26),
(54, 30),
(40, 27);

INSERT INTO Proyecto4_iscdb.TransaccionesCarros
(TotalTransacciones)
VALUES
(1),
(2),
(3);

INSERT INTO Proyecto4_iscdb.BoletosPerdidos
(TotalBoletos, BoletosNoDevueltos, Periodo)
VALUES
(1,2,1),
(1,3,2);