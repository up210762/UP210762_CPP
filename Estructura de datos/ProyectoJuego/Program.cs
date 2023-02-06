﻿using System;
using System.Threading;

namespace PincheProgramaCuleroooooo
{
    class Program
    {
        // Funcion para comparar los números de la matriz
        static bool Comparar(int[,] Matriz, int numero)
        {
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 7; j++)
                {
                    if (Matriz[i, j] == numero)
                    {
                        return false;
                    }
                }
            }
            return true;
        }
        // Impresión de una matriz de tipo int
        static void ImprimirMatrizInt(int[,] Matriz)
        {
            Console.Write("\t");
            for (int i = 0; i <= 4; i++)
            {
                if (i != 0)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.Write((i - 1) + "\t");
                    Console.ForegroundColor = ConsoleColor.White;
                    Console.Write("|");
                    for (int j = 0; j <= 7; j++)
                    {
                        if (j != 0)
                        {
                            Console.Write("\t" + Matriz[i - 1, j - 1] + "\t|");
                            Thread.Sleep(100);
                        }
                    }
                }
                else
                {
                    for (int j = 0; j < 7; j++)
                    {
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.Write("\t" + (j) + "\t");
                    }
                    Console.ForegroundColor = ConsoleColor.White;
                }
                Console.WriteLine("\n\t|\t\t|\t\t|\t\t|\t\t|\t\t|\t\t|\t\t|");
            }
            Thread.Sleep(4000);
        }
        // Impresión de una matriz de tipo string
        static void ImprimirMatrizStr(string[,] Matriz)
        {
            Console.Write("\t");
            for (int i = 0; i <= 4; i++)
            {
                if (i != 0)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.Write((i - 1) + "\t");
                    Console.ForegroundColor = ConsoleColor.White;
                    Console.Write("|");
                    for (int j = 0; j <= 7; j++)
                    {
                        if (j != 0)
                        {
                            Console.Write("\t" + Matriz[i - 1, j - 1] + "\t|");
                            Thread.Sleep(100);
                        }
                    }
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    for (int j = 0; j < 7; j++)
                    {
                        Console.Write("\t" + (j) + "\t");
                    }
                    Console.ForegroundColor = ConsoleColor.White;
                }
                Console.WriteLine("\n\t|\t\t|\t\t|\t\t|\t\t|\t\t|\t\t|\t\t|");
            }
        }
        // Creación de una matriz "Cortina"
        static string[,] LlenadoCortina()
        {
            string[,] Matriz2 = new string[4, 7];
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 7; j++)
                {
                    Matriz2[i, j] = "*";
                }
            }
            return Matriz2;
        }
        // Función para intercambio de datos entre las matrices
        static string[,] Juego(int[,] Matriz, string[,] Matriz2, int a, int b)
        {
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 7; j++)
                {
                    if (i == a && j == b)
                    {
                        Matriz2[i, j] = Convert.ToString(Matriz[a, b]);
                    }
                }
            }
            return Matriz2;
        }
        public static (int, int) RecoleccionDatos(string[,] Matriz2)
        {
            Console.WriteLine("Escribe la posicion que quieras abrir: ");
            string x = Console.ReadLine();
            while (x.Contains(',') == false)
            {
                Console.Clear();
                ImprimirMatrizStr(Matriz2);
                Console.WriteLine("Error de ingreso...");
                Console.WriteLine("Intente otra vez: ");
                x = Console.ReadLine();
            }
            while (x.Length != 3)
            {
                Console.Clear();
                ImprimirMatrizStr(Matriz2);
                Console.WriteLine("Longitud incorrecta, por favor escriba otra vez la coordenada: ");
                x = Console.ReadLine();
            }
            int a = Int32.Parse(x.Substring(0, 1));
            int b = Int32.Parse(x.Substring(x.IndexOf(",") + 1));
            while (a > 3 || b > 6)
            {
                Console.Clear();
                Console.WriteLine("Los datos ingresados son muy grandes, por lo tanto no retornan valor...");
                Console.Write("Ingrese un nuevo valor: ");
                x = Console.ReadLine();
                a = Int32.Parse(x.Substring(0, 1));
                b = Int32.Parse(x.Substring(x.IndexOf(",") + 1));
            }
            return (a, b);
        }
        static int[,] LlenadoPrincipal()
        {
            Random num = new Random();
            int[,] Matriz = new int[4, 7];
            for (int i = 0; i < 4; i++) // matriz con numeros random
            {
                for (int j = 0; j < 7; j++)
                {
                    int numero = num.Next(1, 29);
                    while (Comparar(Matriz, numero) == false)
                    {
                        numero = num.Next(1, 29);
                    }
                    Matriz[i, j] = numero;
                }
            }
            return Matriz;
        }
        public static (bool, int) validar(int contador, int numero)
        {
            contador = contador + numero;
            if (contador == 29)
            {
                return (true, 0);
            }
            else
            {
                return (false, contador);
            }
        }
        public static bool NoRepetido(string dato, string[,] Matriz2)
        {
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 7; j++)
                {
                    if (dato == Matriz2[i, j])
                    {
                        return true;
                    }
                }
            }
            return false;
        }
        static void ModoFacil()
        {
            // Llenado de la matriz principal con numeros random, sin repetir
            Random num = new Random();
            int[,] Matriz = new int[4, 7];
            int count = 0;
            string[,] Matriz2 = new string[4, 7];
            Matriz2 = LlenadoCortina(); // matriz con asteriscos
            Matriz = LlenadoPrincipal();
            // Recolección de datos e impresión de matriz
            ImprimirMatrizInt(Matriz);
            Console.Clear();
            while (count < 14)
            {
                int contador = 0, a = 0, b = 0;
                bool Valido = false;
                ImprimirMatrizStr(Matriz2);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                //Verifica que los números no estén duplicados
                /*###############################################################*/
                while (NoRepetido(Convert.ToString(Matriz[a, b]), Matriz2) == true)
                {
                    Console.WriteLine("El número está repetido...");
                    (a, b) = RecoleccionDatos(Matriz2);
                    (Valido, contador) = validar(contador, Matriz[a, b]);
                }
                /*###############################################################*/
                Matriz2 = Juego(Matriz, Matriz2, a, b);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                while (NoRepetido(Convert.ToString(Matriz[a, b]), Matriz2) == true)
                {
                    Console.WriteLine("El número está repetido...");
                    (a, b) = RecoleccionDatos(Matriz2);
                    (Valido, contador) = validar(contador, Matriz[a, b]);
                }
                Matriz2 = Juego(Matriz, Matriz2, a, b);
                if (Valido == true)
                {
                    Console.Clear();
                    Console.WriteLine("Números correctos...");
                    count += 1;
                    Console.WriteLine("Cantidad de aciertos: " + count);
                }
                else
                {
                    Console.Clear();
                    Console.WriteLine("Números incorrectos...");
                    count = 0;
                    Matriz2 = LlenadoCortina();
                    Console.WriteLine("Cantidad de aciertos: " + count);
                    Thread.Sleep(2000);
                    Console.Clear();
                    Console.WriteLine("Demos otro repaso a la tabla...");
                    ImprimirMatrizInt(Matriz);
                }

                Thread.Sleep(2000);
                Console.Clear();
            }
            Console.WriteLine("¡Felicidades!, has ganado");
            Console.Read();
        }

        static void ModoDificil()
        {
            // Llenado de la matriz principal con numeros random, sin repetir
            Random num = new Random();
            int[,] Matriz = new int[4, 7];
            int count = 0;
            string[,] Matriz2 = new string[4, 7];
            Matriz2 = LlenadoCortina(); // matriz con asteriscos
            Matriz = LlenadoPrincipal();
            // Recolección de datos e impresión de matriz
            ImprimirMatrizInt(Matriz);
            Console.Clear();
            while (count < 14)
            {
                int contador = 0, a = 0, b = 0;
                bool Valido = false;
                ImprimirMatrizStr(Matriz2);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                //Verifica que los números no estén duplicados
                /*###############################################################*/
                while (NoRepetido(Convert.ToString(Matriz[a, b]), Matriz2) == true)
                {
                    Console.WriteLine("El número está repetido...");
                    (a, b) = RecoleccionDatos(Matriz2);
                    (Valido, contador) = validar(contador, Matriz[a, b]);
                }
                /*###############################################################*/
                Matriz2 = Juego(Matriz, Matriz2, a, b);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                while (NoRepetido(Convert.ToString(Matriz[a, b]), Matriz2) == true)
                {
                    Console.WriteLine("El número está repetido...");
                    (a, b) = RecoleccionDatos(Matriz2);
                    (Valido, contador) = validar(contador, Matriz[a, b]);
                }
                Matriz2 = Juego(Matriz, Matriz2, a, b);
                if (Valido == true)
                {
                    Console.Clear();
                    Console.WriteLine("Números correctos...");
                    count += 1;
                    Console.WriteLine("Cantidad de aciertos: " + count);
                }
                else
                {
                    Console.Clear();
                    Console.WriteLine("Números incorrectos...");
                    count = 0;
                    Matriz2 = LlenadoCortina();
                    Console.WriteLine("Cantidad de aciertos: " + count);
                    Thread.Sleep(2000);
                    Console.Clear();
                    Console.WriteLine("Demos otro repaso a la tabla...");
                    ImprimirMatrizInt(Matriz);
                }

                Thread.Sleep(4000);
                Console.Clear();
            }
            Console.WriteLine("¡Felicidades!, has ganado");
            Console.Read();
        }
        static void Escribir(int velocidad, string texto)
        {
            string texto2 = "";
            for (int i = 0; i < texto.Length; i++)
            {
                Console.Clear();
                texto2 = texto2 + texto[i].ToString();
                Console.WriteLine(texto2 + "|");
                Thread.Sleep(velocidad);
                Console.Clear();
                Console.WriteLine(texto2 + " ");
                Thread.Sleep(velocidad);
            }
        }
        static (bool, int) EntradaInvalida(string modo, bool success)
        {
            int x = 0;
            while (success == false)
            {
                Console.Clear();
                Console.WriteLine("Entrada no válida");
                Console.WriteLine("¿Qué modo prefieres jugar?");
                Console.WriteLine("1. Fácil");
                Console.WriteLine("2. Dificil");
                modo = Console.ReadLine();
                success = Int32.TryParse(modo, out x);
            }
            return (success, x);
        }
        static void Main(string[] args)
        {
            Escribir(100, "Bienvenido a nuestro memorama");
            Thread.Sleep(3000);
            Console.Clear();
            Escribir(100, "¿En qué modo prefieres jugar?");
            Console.WriteLine("1. Fácil");
            Console.WriteLine("2. Dificil");
            string modo = Console.ReadLine();
            bool success = Int32.TryParse(modo, out int x);
            while (modo != "1" || modo != "2")
            {

                Console.Clear();
                Console.WriteLine("Modo no válido");
                Console.WriteLine("¿Qué modo prefieres jugar?");
                Console.WriteLine("1. Fácil");
                Console.WriteLine("2. Dificil");
                modo = Console.ReadLine();
                success = Int32.TryParse(modo, out x);
                if (modo == "1" || modo == "2")
                {
                    break;
                }
            }
            if (modo == "1")
            {
                Console.Clear();
                Escribir(100,"Bienvenido al modo fácil");
                Thread.Sleep(2000);
                Console.Clear();
                ModoFacil();
            }
            else
            {
                Console.Clear();
                Escribir(100,"Bienvenido al modo fácil");
                Thread.Sleep(2000);
                Console.Clear();
                ModoDificil();
            }
        }
    }
}