using System;
using System.Linq;

/*
class Program
{
    static void Main(string[] args)
    {
        // Crea una matriz de 4x7
        int[,] matriz = new int[4, 7];

        // Crea una lista de números del 1 al 28 (sin incluir el 29)
        var numeros = Enumerable.Range(1, 28).ToList();

        // Desordena la lista de números
        var rnd = new Random();
        numeros = numeros.OrderBy(x => rnd.Next()).ToList();

        // Recorre las filas y columnas de la matriz
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 7; j++)
            {
                // Asigna un número aleatorio de la lista a la posición i, j de la matriz
                matriz[i, j] = numeros[0];
                // Elimina el número asignado de la lista para evitar repetición
                numeros.RemoveAt(0);
            }
        }

        // Imprime la matriz
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 7; j++)
            {
                Console.Write(matriz[i, j] + " ");
            }
            Console.WriteLine();
        }
    }
}
*/
namespace PincheProgramaCuleroooooo
{
    class Program
    {
        static void Main(string[] args)
        {
            Random num = new Random();
            int [,] Matriz = new int[4,7];
            int validar = 0;
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 7; j++)
                {
                    int numero = num.Next(1,29);
                    while (validar == 0)
                    {
                        int k, l;
                        for (k = 0; k < 4; k ++)
                        {
                            for (l = 0; l < 7; l++)
                            {
                                if (numero == Matriz[k, l])
                                {
                                    validar = 0;
                                }
                            }
                        }
                        numero = num.Next(1,29);
                    }
                    Matriz[i,j] = numero;
                }
            }
        }
    }
}
            