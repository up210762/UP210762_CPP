/* Unidad 1. Tipos de datos
    Autor: Dónovan Alonso Hernandez Carmona
    Fecha: 15/09/2022
    Descripción: Muestra los diferentes tipos de datos en c++
*/

//Libreria para manejo de entradas y salidas de pantalla
#include <iostream>
//libreria para el uso de printf y scanf
#include <stdio.h>

//Uso del namespace para evitar el std::
using namespace std;

//Función principal de tipo entero
int main()
{
    int entero = 21;
    float flotante = 3.4e38;
    double grande = 2.5654;
    char caracter = '@';
    cout << "Este programa muestra los tipos de datos. \n";
    cout << "El número entero es: " << entero << endl;
    cout << "El tamaño del entero es: " << sizeof(entero) << " bytes" << endl;
    
    cout << "El número entero es: " << caracter << endl;
    cout << "El tamaño del entero es: " << sizeof(caracter) << " bytes" << endl;
    //getchar();
    return 0;
/*

    cout << "Este programa muestra " << entero << endl;
    cout << "El tamaño del flotante es " << sizeof(flotante) << endl;
*/
}