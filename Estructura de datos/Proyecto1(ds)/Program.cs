using System;

namespace PincheProgramaCuleroooooo
{
    class Program
    {
        static void Main(string[] args)
        {
            int posi=0, posj=0, mayor=0;
            int[,] matriz = new int[4, 7];
            Random aleatorio = new Random();
            for (int i=0; i<4; i++)
            {
                for (int j=0; j<7; j++)
                {
                    int n = aleatorio.Next(1,28);
                    matriz[i, j] = n;
                }
            }
            for (int i=0; i < 4; i++)
            {
                for (int j=0; j < 7; j++)
                {
                    Console.Write(matriz[i, j] + "\t");
                }
            Console.WriteLine();
            }
            
        }
    }
}
