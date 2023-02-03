CREATE DATABASE Proyecto4_iscdb;

USE DATABASE Proyecto4_iscdb;

CREATE TABLE Proyecto4_iscdb.Cajero(
	Id int auto_increment not null,
    Nombre nvarchar(50) not null,
    Km decimal(18,2) not null,
    Activo bit null,
    Borrado bit null
    );