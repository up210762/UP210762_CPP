<center>
<h1>Fusión.py<h1>
</center>

<h3>Es el resultado funcional de la fusión del programa "Agrupados.py" y "Cuartiles.py", donde se busca unificar los resultados y poder obtener los gráficos y los datos completos, sin necesidad de hacer reescritura manual doble.</h3>
<br>
<center>
<h1>Variables</h1>
</center>
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
<br>

![IMAGEN](/IMAGENES/MEDIA.png)

<br>
</center>
<h3><div align = "left">En esta parte del códio se hizo apoyo del códogo de la sumatoria para la varianza, donde posteriormente se hizo la división por el total de números representado por la variable "longitud".</div></h3>
<br>

![IMAGEN](/IMAGENES/CODIGO%20MEDIA.png)

<br>
<center>
<h2>MEDIANA</h2>

![IMAGEN](/IMAGENES/MEDIANA.png)

</center>
<br>
<h3><div align = "left">Para cumplir la fórmula se hizo el siguiente algoritmo, donde el rango de las categorías se sacó del apartado de la regla de Sturges.</div></h3>

![IMAGEN](/IMAGENES/CODIGO%20MEDIANA.png)

<br>

<center><h2>MODA</h2></center>

<center>

![IMAGEN](/IMAGENES/MODA.png)

</center>
<br>
<h3><div align = "left">Esta fórmula es un poco más dificil que las anteriores, pues se debe obtener el límite inferior, número anterior a la frecuencia absoluta más alta y también el número que le sigue. Para resolver este problema se diseñó un algoritmo capaz de hacer la búsqueda de manera automática.</div></h3>
<br>
<h1><div align = "left">Medidas de dispersión</div></h1>
<br>
<center>
<h2>Varianza</h2>

![IMAGEN](/IMAGENES/VARIANZA.png)

<br>

![IMAGEN](/IMAGENES/CODIGO%20VARIANZA.png)
<br>
</center>

<h3><div align = "left">Primero se realiza una sumatoria de la multiplicación de las marcas de clase por las frecuencias absolutas y se dividen entre la longitud para sacar la media aritmética. Después se hace la sumatoria del la multiplicación de las frecuencias absolutas por el cuadrado de las diferencias de las marcas de clase menos la media aritmética. Por último, se dividirá el resultado de lo anterior entre el total de números introducidos menos uno.</div></h3>
<br>
<center>
<h2>Desviación estándar</h2>
<br>

![IMAGEN](/IMAGENES/DESVIACI%C3%93N%20EST%C3%81NDAR.png)

<br>

![IMAGEN](/IMAGENES/CODIGO%20DESVIACI%C3%93N%20EST%C3%81NDAR.png)

</center>
<br>
<h3><div align = "left">Para obtener la desviación estándar se debe sacar la raíz cuadrada de la varianza, para ello se utilizó la librería numpy.</div></h3>
<br>
<center>
<h2>Coeficiente de variación</h2>
<br>

![IMAGEN](/IMAGENES/COEFICIENTE%20DE%20VARIACI%C3%93N.png)

<br>


![IMAGEN](/IMAGENES/CODIGO%20COFICIENTE%20DE%20VARIACI%C3%93N.png)
<br>
</center>
<h3><div align = "left">Para el cociente de variación solo se divide la desviación estándar entre la media aritmética y el resultado se multiplica por cien, dejando un resultado porcentual.</div></h3>
<br>
</center>
<br>
<center><h2>Cuartiles</h2></center>
<br>
<h3>Para este tramo de código, se separó en dos programas diferentes, además se hizo uso de muchas condicionales para lograr que el algoritmo se acercara al resultado más correcto. Los cuartiles siguiendo la siguiente fórmula:</h3>

<center>

![IMAGEN](/IMAGENES/CUARTILES.png)

![IMAGEN](/IMAGENES/CODIGO%20CUARTILES.png)

<br>
<h3><div align = "left">El "controlador" del cuartil proviene a partir de la operación k*N/4, pues el resultado que genere se tendrá que buscar que entre en las frecuencias absolutas acumuladas. Derivado de ello es que cambiarán los valores.</div></h3>

</center>
<br>
<h4><div align = "left">Para probar el programa intoduzca los siguientes 25 números: 40, 37, 60, 10, 30, 45, 55, 27, 40, 70, 30, 50, 35, 40, 60, 80, 50, 60, 65, 50, 55, 40, 35, 48, 50</div></h4>

<center>
<table class="default">
    <tr>
        <td>Categorías</td>
        <td>Xi</td>
        <td>fi</td>
        <td>Fi</td>
        <td>fr</td>
        <td>Fr</td>
        <td>hi</td>
    <tr>
    <tr>
        <td>10-22</td>
        <td>16</td>
        <td>1</td>
        <td>1</td>
        <td>0.04</td>
        <td>0.04</td>
        <td>4%</td>
    <tr>
    <tr>
        <td>22-34</td>
        <td>28</td>
        <td>3</td>
        <td>4</td>
        <td>0.12</td>
        <td>0.16</td>
        <td>12%</td>
    <tr>
    <tr>
        <td>34-46</td>
        <td>40</td>
        <td>8</td>
        <td>12</td>
        <td>0.32</td>
        <td>0.48</td>
        <td>32%</td>
    <tr>
    <tr>
        <td>46-58</td>
        <td>52</td>
        <td>7</td>
        <td>19</td>
        <td>0.28</td>
        <td>0.76</td>
        <td>28%</td>
    <tr>
    <tr>
        <td>58-70</td>
        <td>64</td>
        <td>4</td>
        <td>23</td>
        <td>0.16</td>
        <td>0.92</td>
        <td>16%</td>
    <tr>
    <tr>
        <td>70-82</td>
        <td>76</td>
        <td>2</td>
        <td>25</td>
        <td>0.08</td>
        <td>1</td>
        <td>8%</td>
    <tr>
</table>
<br>
<table class="default">
    <tr>
        <td>MTC</td>
        <td>MD</td>
        <td>Cuartiles</td>
        <td>Otros</td>
    <tr>
    <tr>
        <td>X=47.68</td>
        <td>R=70</td>
        <td>Q1=37.37</td>
        <td>CA=0.16</td>
    <tr>
    <tr>
        <td>Me=46.85</td>
        <td>s^2=226.5583</td>
        <td>Q2=46.85</td>
        <td>k=5.64</td>
    <tr>
    <tr>
        <td>Mo=44</td>
        <td>s=15.0518</td>
        <td>Q3=57.57</td>
        <td>A=12</td>
    <tr>
    <tr>
        <td></td>
        <td>Cv=31.56%</td>
        <td></td>
        <td></td>
    <tr>
</table>
</center>

<h3><FONT color="FF00">Nota: los resultados expuestos en las tablas son cálculos hechos a mano. La diferencia de decimales puede ser consecuencia del redondeo al momento de hacer los cálculos en papel.</FONT></h3>