<center>
<h1>Agrupados.py<h1>
</center>

<h1>Variables</h1>
<br>
<h3>Para el control de las variables, se ha dividido en dos partes: variables estáticas y variables dinámicas, donde las variables estáticas son las que se presentarán como salida en print al usuario.</h3>
<center>

![IMAGEN](/IMAGENES/VARIABLES.png)

</center>
<br>
<h1>Medidas de tendencia central (MTC)</h1>
<br>
<h3>En las medidas de tendencia central, los valores que se buscan obtener son media mediana y moda, obtenidas a partir de las siguientes fórmulas:</h3>
<br>
<center>
<h2>MEDIA</h2>

![IMAGEN](/IMAGENES/MEDIA.png)
<br>
<h3><div align = "left">En esta parte del códio se hizo apoyo del códogo de la sumatoria para la varianza, donde posteriormente se hizo la división por el total de números representado por la variable "longitud".</div></h3>
<br>

![IMAGEN](/IMAGENES/CODIGO%20MEDIA.png)

<br>
<h2>MEDIANA</h2>

![IMAGEN](/IMAGENES/MEDIANA.png)
<br>
<h3><div align = "left">Para cumplir la fórmula se hizo el siguiente algoritmo, donde el rango de las categorías se sacó del apartado de la regla de Sturges.</div></h3>

![IMAGEN](/IMAGENES/CODIGO%20MEDIANA.png)

<br>
<h2>MODA</h2>

![IMAGEN](/IMAGENES/MODA.png)
<br>
<h3><div align = "left">Esta fórmula es un poco más dificil que las anteriores, pues se debe obtener el límite inferior, número anterior a la frecuencia absoluta más alta y también el número que le sigue. Para resolver este problema se diseñó un algoritmo capaz de hacer la búsqueda de manera automática.</div></h3>
<br>
<h1><div align = "left">Medidas de dispersión</div></h1>
<br>
<h2>Varianza</h2>

![IMAGEN](/IMAGENES/VARIANZA.png)

<br>

![IMAGEN](/IMAGENES/CODIGO%20VARIANZA.png)
<br>
<h3><div align = "left">Primero se realiza una sumatoria de la multiplicación de las marcas de clase por las frecuencias absolutas y se dividen entre la longitud para sacar la media aritmética. Después se hace la sumatoria del la multiplicación de las frecuencias absolutas por el cuadrado de las diferencias de las marcas de clase menos la media aritmética. Por último, se dividirá el resultado de lo anterior entre el total de números introducidos menos uno.</div></h3>
<br>
<h2>Desviación estándar</h2>
<br>

![IMAGEN](/IMAGENES/DESVIACI%C3%93N%20EST%C3%81NDAR.png)

<br>

![IMAGEN](/IMAGENES/CODIGO%20DESVIACI%C3%93N%20EST%C3%81NDAR.png)
<br>
<h3><div align = "left">Para obtener la desviación estándar se debe sacar la raíz cuadrada de la varianza, para ello se utilizó la librería numpy.</div></h3>
<br>
<h2>Coeficiente de variación</h2>
<br>

![IMAGEN](/IMAGENES/COEFICIENTE%20DE%20VARIACI%C3%93N.png)

<br>


![IMAGEN](/IMAGENES/CODIGO%20COFICIENTE%20DE%20VARIACI%C3%93N.png)
<br>
<h3><div align = "left">Para el cociente de variación solo se divide la desviación estándar entre la media aritmética y el resultado se multiplica por cien, dejando un resultado porcentual.</div></h3>
<br>
</center>

<center><h1>Cuartiles.py<h1></center>
<h3>Para este programa se generó un código con muchas condicionales, pues son requeridas para obtener el resultado correcto de los cuartiles siguiendo la siguiente fórmula:</h3>

<center>

![IMAGEN](/IMAGENES/CUARTILES.png)

![IMAGEN](/IMAGENES/CODIGO%20CUARTILES.png)

<br>
<h3><div align = "left">El "controlador" del cuartil proviene a partir de la operación k*N/4, pues el resultado que genere se tendrá que buscar que entre en las frecuencias absolutas acumuladas. Derivado de ello es que cambiarán los valores.</div></h3>

</center>
