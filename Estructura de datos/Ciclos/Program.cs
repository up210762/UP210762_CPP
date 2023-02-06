using System;


/*
namespace Ciclos
{
    class Program
    {
        static void Main(string[] arg)
        {
            int k = 0;
            int [] n1 = {10,20,30,40,50,60,70,80};
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 2; j++)
                    Console.Write("{n1}", n1[k]);
                    k = k + 1;

        }
    }
}
*/
/*
namespace Metodos
{
   class Program
    {
        static int PlusMethod(int x,int y)
        {
            return x + y;
        }
        static double PlusMethod(double x,double y)
        {
            return x + y;
        }

        static int PlusMethod(int x,int y, int z)
        {
            return x + y + z;
        }
        static void Main(string[] args)
        {
            int myNum1 = PlusMethod(8,5);
            int myNum3 = PlusMethod(5,6,7);
            double myNum2 = PlusMethod(4.3, 6.26);
            Console.WriteLine("Int: " + myNum1);
            Console.WriteLine("Double: " + myNum2);
            Console.WriteLine("Int 3 params: " + myNum3);
        }
    }
}
*/
/*
namespace ISC4B_Random
{
    class Program
    {
        static void Main(string[] args)
        {
            Random x = new Random();
            for(int i = 0; i < 100; i++)
            {
                int aleatorio = x.Next(1000);
                Console.WriteLine("Número aleatorio: " + aleatorio);
            }
            Console.ReadLine();
        }
    }
}
*/
/*
namespace Adivina
{
    class Program
    {
        static void Main(string[] args)
        {
            int i;
            int y = 0;
            Random x = new Random();
            int j = x.Next(0,10);
            Console.WriteLine("Escribe un úmero entre 0 y 10: ");
            i = int.Parse(Console.ReadLine());
            if(i!=j)
            {
                while (i != j)
                {
                    if(y == 4){
                        Console.WriteLine("Has perdido");
                        break;
                    }
                    else{
                        Console.WriteLine("Número incorrecto, intenta otra vez: ");
                        if(i > j)
                        {
                            Console.WriteLine("Número muy grande");
                            i = int.Parse(Console.ReadLine());
                            y = y + 1;
                        }
                        else if(i < j)
                        {
                            Console.WriteLine("Número muy pequeño");
                            i = int.Parse(Console.ReadLine());
                            y = y + 1;
                        }
                    }
                    
                }
            }
            else{
                
            }

        }
    }
}
*/
public class Example
{
	public static void Main()
	{
		string str = "q";

		bool success = Int32.TryParse(str, out int x);	// or, use `int.TryParse()`

		if (success) {
			Console.WriteLine(x);
		}
		else {
			Console.WriteLine("Input string is invalid.");
		}
        Console.WriteLine(success + " " + x);
	}
}