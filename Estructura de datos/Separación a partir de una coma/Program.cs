using System;
using System.IO;

namespace Separar
{
    class Program
    {
        static void Función1()
        {
            Console.WriteLine("Dónovan,Alonso,Hernández,Carmona,20 años,Aguascalíentes,Masculino,Soltero");
            string texto = Console.ReadLine();
            string[] textoSeparado = texto.Split(',');
            Console.WriteLine("");
            Console.Write("La separación de variables queda como: ");
            for (int i = 0; i < textoSeparado.Length; i++)
            {
                Console.Write(textoSeparado[i]);
            }
            Console.WriteLine("");
            Console.Write("La separación de variable es: ");
            foreach(string palabra in textoSeparado)
            {
                Console.WriteLine(palabra);
            }
            Console.Read();
            //Validacion de que la variable sea un número
            try 
            {
                int num = Convert.ToInt32(textoSeparado[4]);
                Console.WriteLine(num);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                Console.WriteLine("La variable no se puede convertir en entero");
            }
        }
        static void Main(string[] args)
        {
            string line = "";
            try
            {
                StreamReader sr = new StreamReader("/home/d2022f/Documents/UP210762_CPP/Estructura de datos/Separación a partir de una coma/texto.txt");
                line = sr.ReadLine();
                string [] cadenaCompleta = line.Split(',');
                Console.WriteLine("Dónovan,Alonso,Hernández,Carmona,20,Aguascalíentes,Masculino,Soltero");
                Console.Write("Escribe las cadenas a separar: ");
                string texto = Console.ReadLine();
                string [] textoSeparado = texto.Split(',');
                int contador = 0;
                while (line != null && contador < textoSeparado.Length)
                { 
                    // if (texto == line || foreach(textoSeparado[contador] in cadenaCompleta))
                    // {
                    //     Console.WriteLine(textoSeparado[contador]);
                    //     contador += 1;
                    // }
                    
                    contador += 1;
                    if(textoSeparado[contador] == cadenaCompleta[contador])
                    {
                        Console.WriteLine(textoSeparado[contador]);
                    }
                    else
                    {
                        continue;
                    }
                }
                sr.Close();
            }
            catch(Exception e)
            {
                Console.WriteLine("Archivo no encontrado. " + e.Message);

            } 
        }
    }

}
