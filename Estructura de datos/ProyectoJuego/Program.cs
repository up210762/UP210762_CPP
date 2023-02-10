using System;
using System.Threading;
using System.Diagnostics;

namespace PincheProgramaCuleroooooo
{
    class Program
    {
        // Compara los números de la matriz
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
        static void ImprimirMatrizInt(int vel, int[,] Matriz)
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
                            Thread.Sleep(vel);
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
        static void ImprimirMatrizStr(int vel, string[,] Matriz)
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
                            Thread.Sleep(vel);
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
        // Intercambio de datos entre las matrices
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
        // Entrada de datos por teclado y validación de los mismos
        public static (int, int) RecoleccionDatos(string[,] Matriz2)
        {
            int a = 0, b = 0, c = 0;
            Console.WriteLine("Escribe la posicion que quieras abrir: ");
            string x = Console.ReadLine();
            while (c == 0 || x == "")
            {
                while (x != "")
                {
                    if (MensajeError(x.Substring(0, 1)) == false && MensajeError(x.Substring(x.IndexOf(',') + 1)) == false && x.Length == 3 && x.Contains(',') == true)
                    {
                        a = Int32.Parse(x.Substring(0, 1));
                        b = Int32.Parse(x.Substring(x.IndexOf(",") + 1));
                        c = c + 1;
                        break;
                    }
                    else if (MensajeError(x.Substring(0, 1)) == true || MensajeError(x.Substring(x.IndexOf(',') + 1)) == true || x.Length > 0 || x.Contains(',') == false)
                    {
                        while (MensajeError(x.Substring(0, 1)) == true || MensajeError(x.Substring(x.IndexOf(",") + 1)) == true || x.Length != 3 || x.Contains(",") == false)
                        {


                            if (x.Contains(",") == false)
                            {
                                Console.Clear();
                                ImprimirMatrizStr(0, Matriz2);
                                Console.WriteLine("Error de ingreso...");
                                Console.WriteLine("Intente otra vez: ");
                                x = Console.ReadLine();
                                if (x == "")
                                {
                                    break;
                                }
                                MensajeError(x.Substring(0, 1));
                                MensajeError(x.Substring(x.IndexOf(",") + 1));
                                continue;
                            }
                            else if (x.Length != 3)
                            {
                                Console.Clear();
                                ImprimirMatrizStr(0, Matriz2);
                                Console.WriteLine("Longitud incorrecta, por favor escriba otra vez la coordenada: ");
                                x = Console.ReadLine();
                                if (x == "")
                                {
                                    break;
                                }
                                MensajeError(x.Substring(0, 1));
                                MensajeError(x.Substring(x.IndexOf(",") + 1));
                                continue;
                            }
                            if ((MensajeError(x.Substring(0, 1)) == true || MensajeError(x.Substring(x.IndexOf(",") + 1)) == true) && x != "")
                            {
                                Console.Clear();
                                ImprimirMatrizStr(0, Matriz2);
                                Console.WriteLine("Valores no válidos...");
                                Console.WriteLine("Intente otra vez: ");
                                x = Console.ReadLine();
                                if (x == "")
                                {
                                    break;
                                }
                                MensajeError(x.Substring(0, 1));
                                MensajeError(x.Substring(x.IndexOf(",") + 1));
                                continue;
                            }
                        }

                    }
                }
                if (x == "")
                {
                    Console.Clear();
                    ImprimirMatrizStr(0, Matriz2);
                    Console.WriteLine("¡No has ingresado valores!");
                    Console.WriteLine("Intenta otra vez...");
                    x = Console.ReadLine();
                    continue;
                }
            }
            return (a, b);
        }
        // Reproduce una canción
        static void Cancion()
        {
            try
            {
                using (Process myProcess = new Process())
                {
                    myProcess.StartInfo.UseShellExecute = false;
                    myProcess.StartInfo.FileName = "./bash.sh";
                    myProcess.StartInfo.CreateNoWindow = true;
                    myProcess.Start();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
        // Llenado de la matriz con números random, de manea aleatoria
        static int[,] LlenadoPrincipal()
        {
            Random num = new Random();
            int[,] Matriz = new int[4, 7];
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
            return Matriz;
        }
        // Función para el borrado de la tabla string por pocisión
        public static string [,] BorradoModoFacil(int[] vector, int [,] Matriz, string[,] Matriz2)
        {
            for (int i = 0; i < 2; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    for (int k = 0; k < 7; k++)
                    {
                        if (Matriz[j,k] == vector[i])
                        {
                            Matriz2[j,k] = "*";
                        }
                    }
                }
            }
            return Matriz2;
        }
        // Validación de la sumatroria de los números destapados
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
        // Validación de entrada dosnde se limita la apertura de las casillas a una sola vez
        public static bool NoRepetido(string dato, string[,] Matriz2)
        {
            bool repetido = false;
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 7; j++)
                {
                    if (dato == Matriz2[i, j])
                    {
                        repetido = true;
                        return repetido;
                    }
                }
            }
            return repetido;
        }
        //Limitación de entrada a ciertos datos
        static bool MensajeError(string dato)
        {
            if (dato == "1" || dato == "2" || dato == "3" || dato == "4" || dato == "5" || dato == "6" || dato == "0")
            {
                return false;
            }
            else if (dato == "")
            {
                return true;
            }
            else
            {
                return true;
            }
        }
        // Ejecución del modo fácil
        static void ModoFacil()
        {
            Random num = new Random();
            int[,] Matriz = new int[4, 7];
            int count = 0;
            string[,] Matriz2 = new string[4, 7];
            int [] vector = new int[2];
            Matriz2 = LlenadoCortina(); 
            Matriz = LlenadoPrincipal();
            ImprimirMatrizStr(100, Matriz2);
            Console.Clear();
            while (count < 14)
            {
                int contador = 0, a = 0, b = 0;
                bool Valido = false;
                ImprimirMatrizStr(0, Matriz2);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                while (NoRepetido(Convert.ToString(Matriz[a, b]), Matriz2) == true)
                {

                    Console.Clear();
                    ImprimirMatrizStr(0, Matriz2);
                    Console.WriteLine("El número está repetido...");
                    (a, b) = RecoleccionDatos(Matriz2);
                    (Valido, contador) = validar(contador, Matriz[a, b]);
                }
                Matriz2 = Juego(Matriz, Matriz2, a, b);
                vector[0] = Matriz[a,b];
                Console.Clear();
                ImprimirMatrizStr(0, Matriz2);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                while (NoRepetido(Convert.ToString(Matriz[a, b]), Matriz2) == true)
                {

                    Console.Clear();
                    ImprimirMatrizStr(0, Matriz2);
                    Console.WriteLine("El número está repetido...");
                    (a, b) = RecoleccionDatos(Matriz2);
                    (Valido, contador) = validar(contador, Matriz[a, b]);
                }
                Matriz2 = Juego(Matriz, Matriz2, a, b);
                vector[1] = Matriz[a,b];
                Console.Clear();
                ImprimirMatrizStr(0, Matriz2);
                if (Valido == true)
                {
                    Console.WriteLine("Números correctos...");
                    count += 1;
                    Console.WriteLine("Cantidad de aciertos: " + count);
                }
                else
                {
                    Console.WriteLine("Números incorrectos...");
                    count = 0;
                    Matriz2 = BorradoModoFacil(vector, Matriz, Matriz2);
                    Console.WriteLine("Cantidad de aciertos: " + count);
                    
                }

                Thread.Sleep(4000);
                Console.Clear();
            }
            ImprimirMatrizStr(200, Matriz2);
            Console.WriteLine("¡Felicidades!, has ganado");
        }
        // Ejecución del modo dificil
        static void ModoDificil()
        {
            Random num = new Random();
            int[,] Matriz = new int[4, 7];
            int count = 0;
            string[,] Matriz2 = new string[4, 7];
            Matriz2 = LlenadoCortina();
            Matriz = LlenadoPrincipal();
            ImprimirMatrizInt(100, Matriz);
            Console.Clear();
            while (count < 14)
            {
                int contador = 0, a = 0, b = 0;
                bool Valido = false;
                ImprimirMatrizStr(100, Matriz2);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                while (NoRepetido(Convert.ToString(Matriz[a, b]), Matriz2) == true)
                {
                    Console.Clear();
                    ImprimirMatrizStr(0, Matriz2);
                    Console.WriteLine("El número está repetido...");
                    (a, b) = RecoleccionDatos(Matriz2);
                    (Valido, contador) = validar(contador, Matriz[a, b]);
                }
                Matriz2 = Juego(Matriz, Matriz2, a, b);
                (a, b) = RecoleccionDatos(Matriz2);
                (Valido, contador) = validar(contador, Matriz[a, b]);
                while (NoRepetido(Convert.ToString(Matriz[a, b]), Matriz2) == true)
                {
                    Console.Clear();
                    ImprimirMatrizStr(0, Matriz2);
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
                    ImprimirMatrizInt(100, Matriz);
                }

                Thread.Sleep(4000);
                Console.Clear();
            }
            ImprimirMatrizStr(200, Matriz2);
            Console.WriteLine("¡Felicidades!, has ganado");
        }
        // Animación de escritura
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
        // Limmite la elección de los modos a la entrada del número "1" y el número "2".
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
        // Ejecución del código
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
                if (modo == "1" || modo == "2")
                {
                    break;
                }
                Console.Clear();
                Console.WriteLine("Modo no válido");
                Console.WriteLine("¿Qué modo prefieres jugar?");
                Console.WriteLine("1. Fácil");
                Console.WriteLine("2. Dificil");
                modo = Console.ReadLine();
                success = Int32.TryParse(modo, out x);
            }
            if (modo == "1")
            {
                Console.Clear();
                Cancion();
                Escribir(100, "Bienvenido al modo fácil");
                Thread.Sleep(2000);
                Console.Clear();
                ModoFacil();
            }
            else
            {
                Console.Clear();
                Cancion();
                Escribir(100, "Bienvenido al modo dificil");
                Thread.Sleep(2000);
                Console.Clear();
                ModoDificil();
            }
        }
    }
}