SELECT Count(*) As JugadoresEstaturas, Estatura FROM `FirstDataBase`.`JugadorSinRelacion`
WHERE Estatura between 1.70 and 1.76
Group by Estatura