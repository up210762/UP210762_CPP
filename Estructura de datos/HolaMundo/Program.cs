// See https://aka.ms/new-console-template for more information
using System;
/*################################################################################################################################################*/
/*
namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            int myNum = 15;
            string name = "John";
            bool yay = true;
            bool nay = false;

            Console.WriteLine("Mi nombre es " + name + " y tnego " + myNum + " años." + " " + nay + " " + yay);
            Console.WriteLine(Convert.ToString(myNum));

        }
    }
}
*/
/*################################################################################################################################################*/
//Conversión implicita
/*
namespace ISC4B_Casting_Implicit
{
    class Program
    {
        static void Main(string[] args)
        {
            int myInt = 9;
            double myDouble = myInt;

            Console.WriteLine(myInt);
            Console.WriteLine(myDouble);

            Console.Read();
        }
    }
}
*/
/*################################################################################################################################################*/
//Conversión explicita
/*
namespace ISC4B_Casting_Explicit
{
    class Program
    {
        static void Main(string[] args)
        {
            double myDouble = 9.78;
            int myInt = (int)myDouble;

            Console.WriteLine(myDouble);
            Console.WriteLine(myInt);

            Console.Read();
        }
    }
}
*/
/*################################################################################################################################################*/
/*
namespace Convertir
{
    class Program
    {
        static void Main(string[] arg)
        {
            int myInt = 10;
            double myDouble = 5.25;
            bool myBool = true;

            Console.WriteLine(Convert.ToString(myInt));
            Console.WriteLine(Convert.ToDouble(myInt));
            Console.WriteLine(Convert.ToInt32(myDouble));
            Console.WriteLine(Convert.ToBoolean(myBool));

            Console.Read();
        }
    }
}
*/
/*################################################################################################################################################*/

/*
namespace Introducir
{
    class Program
    {
        static void Main(string[] arg)
        {
            string name = "John Doe";
            int charPos = name.IndexOf('D');
            string lastname = name.Substring(charPos);
            Console.WriteLine(lastname);
        }
    }
}

namespace Introducir
{
    class Program
    {
        static void Main(string[] arg)
        {
            int k = 0;
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 5; j++)
                {
                    if (i == 4)
                    {
                        k = k + 1;
                        Console.WriteLine("1");
                        break;
                    }
                }
            }
            Console.WriteLine(k);
        }
    }
}
*/
/*

namespace Introducir
{
    class Program
    {
        static void Main(string[] arg)
        {
            int n1[4][2];
            for (int i = 0; i <= 3; i++)
            {
                for (int j = 0; j <= 1; j++)
                {
                    
                }
            }
            Console.WriteLine();
        }
    }
}
*/
/*
class Program
{
    public static void Main(string[] args)
    {
        string x = Console.ReadLine();
        int y = Int32.Parse(x.Substring(0,1));
        int z = Int32.Parse(x.Substring(x.Length - 1, 1));
        Console.WriteLine(y + " " + z);
    }
}
*/
/*
using System.Diagnostics;
using System.ComponentModel;
namespace MyProcessSample
{
    class MyProcess
    {
        static void Main(string[] args)

        {
            System.Diagnostics.ProcessStartInfo procStartInfo = new System.Diagnostics.ProcessStartInfo("gnome-terminal", "ls");
            procStartInfo.RedirectStandardOutput = false;
            procStartInfo.UseShellExecute = false;
            procStartInfo.CreateNoWindow = true;
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.StartInfo = procStartInfo;
            proc.Start();
            Console.WriteLine(proc.StandardOutput.ReadToEnd());

        }

    }
}
*/
using System.Diagnostics;

public class StartingProcesses
{
    public static void Main()
    {
        ProcessStartInfo startInfo = new ProcessStartInfo();
        startInfo.FileName = "/usr/bin/comando";
        startInfo.Arguments = "argumento1";
        Process.Start(startInfo);
    }
}

/*
namespace MyProcessSample
{
    class MyProcess
    {

        public static void Main()
        {
            try
            {
                using (Process myProcess = new Process())
                {
                    myProcess.StartInfo.UseShellExecute = true;
                    // You can start any process, HelloWorld is a do-nothing example.
                    myProcess.StartInfo.FileName = "gnome-terminal";
                    myProcess.StartInfo.Arguments = "play /home/d2022f/Music/Geoxor - Stardust.mp3";
                    myProcess.StartInfo.CreateNoWindow = true;
                    myProcess.Start();
                    Console.Read();
                    
                    // This code assumes the process you are starting will terminate itself.
                    // Given that it is started without a window so you cannot terminate it
                    // on the desktop, it must terminate itself or you can do it programmatically
                    // from this application using the Kill method.
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}
*/

/*
namespace Execute
{
    class Execute
    {
        static void ExecuteCommand()
        {
            string _Command = "ls";
            //Indicamos que deseamos inicializar el proceso cmd.exe junto a un comando de arranque. 
            //(/C, le indicamos al proceso cmd que deseamos que cuando termine la tarea asignada se cierre el proceso).
            //Para mas informacion consulte la ayuda de la consola con cmd.exe /? 
            System.Diagnostics.ProcessStartInfo procStartInfo = new System.Diagnostics.ProcessStartInfo("gnome-terminal", _Command);
            // Indicamos que la salida del proceso se redireccione en un Stream
            procStartInfo.RedirectStandardOutput = true;
            procStartInfo.UseShellExecute = false;
            //Indica que el proceso no despliegue una pantalla negra (El proceso se ejecuta en background)
            procStartInfo.CreateNoWindow = false;
            //Inicializa el proceso
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.StartInfo = procStartInfo;
            proc.Start();
            //Consigue la salida de la Consola(Stream) y devuelve una cadena de texto
            string result = proc.StandardOutput.ReadToEnd();
            //Muestra en pantalla la salida del Comando
            Console.WriteLine(result);
        }
        static void Main(string[] args)
        {
            ExecuteCommand();
        }
    }
}
*/