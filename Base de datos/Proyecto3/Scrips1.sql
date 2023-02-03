ALTER TABLE NacionalidadId
ADD columna_nueva BIT;

ALTER TABLE NacionalidadId
DROP columna_nueva;

ALTER TABLE NacionalidadId
RENAME COLUMN columna_nueva TO columna_nueva2;

alter table JugadorConRelaciones
modify COLUMN Id int auto_increment;

ALTER TABLE NacionalidadId
MODIFY COLUMN Id int PRIMARY KEY AUTO_INCREMENT;

ALTER Table EquipoId
MODIFY COLUMN Id int primary key AUTO_INCREMENT;

ALTER Table PocisionId
MODIFY COLUMN Id int primary key AUTO_INCREMENT;

