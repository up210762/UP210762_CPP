using System;

namespace copia
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
            for (int i = 0; i < 4; i++)
            {
                Console.Write("|");
                for (int j = 0; j < 7; j++)
                {
                    Console.Write("\t" + Matriz[i, j] + "\t|");
                    Thread.Sleep(100);
                }
                Console.WriteLine();
            }
            Thread.Sleep(4000);
        }
        // Impresión de una matriz de tipo string
        static void ImprimirMatrizStr(string[,] Matriz)
        {
            for (int i = 0; i < 4; i++)
            {
                Console.Write("|");
                for (int j = 0; j < 7; j++)
                {
                    Console.Write("\t" + Matriz[i, j] + "\t|");
                    Thread.Sleep(100);
                }
                Console.WriteLine();
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
            return (a, b);
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
                    if (dato == Matriz2[i,j])
                    {
                        return true;
                    }
                }
            }
            return false;
        }
        static void Main(string[] args)
        {
            // Llenado de la matriz principal con numeros random, sin repetir
            Random num = new Random();
            int[,] Matriz = new int[4, 7];
            int count = 0;
            string[,] Matriz2 = new string[4, 7];
            Matriz2 = LlenadoCortina();
            for (int i = 0; i < 4; i++)
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
            // Recolección de datos e impresión de matriz
            ImprimirMatrizInt(Matriz);
            Console.Clear();
            while (count < 28)
            {
                int contador = 0, a = 0, b = 0;
                bool Valido = false;
                ImprimirMatrizInt(Matriz);
                ImprimirMatrizStr(Matriz2);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                //Verifica que los números no estén duplicados
                /*###############################################################*/
                while (NoRepetido(Convert.ToString(Matriz[a,b]),Matriz2) == true)
                {
                    Console.WriteLine("El número está repetido...");
                    (a, b) = RecoleccionDatos(Matriz2);
                    (Valido, contador) = validar(contador, Matriz[a, b]);
                }
                /*###############################################################*/
                Matriz2 = Juego(Matriz, Matriz2, a, b);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                while (NoRepetido(Convert.ToString(Matriz[a,b]),Matriz2) == true)
                {
                    Console.WriteLine("El número está repetido...");
                    (a, b) = RecoleccionDatos(Matriz2);
                    (Valido, contador) = validar(contador, Matriz[a, b]);
                }
                Matriz2 = Juego(Matriz, Matriz2, a, b);
                if (Valido == true)
                {
                    Console.WriteLine("Números correctos...");
                    count += 1;
                }
                else
                {
                    Console.WriteLine("Números incorrectos...");
                    Matriz2 = LlenadoCortina();
                }

                Thread.Sleep(4000);
                Console.Clear();
            }
            Console.WriteLine("¡Felicidades!, has ganado");
            Console.Read();
        }
    }
}