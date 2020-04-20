using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace ConsoleApp1
{
    class Gauss
    {

        int[][] A;
        int[][] B;
        double[] X;


        public void readFromFile()
        {
            try
            {
                //A
                string input = File.ReadAllText(@"C:\Users\wikto\OneDrive\Pulpit\ \semestr IV\MN\Lab3 - Eliminacja Gauss'a\C# gauss\ConsoleApp1\A.txt");
                input.ToCharArray();
                
                //B
                input = File.ReadAllText(@"C:\Users\wikto\OneDrive\Pulpit\ \semestr IV\MN\Lab3 - Eliminacja Gauss'a\C# gauss\ConsoleApp1\B.txt");
              

            }
            catch (IOException e)
            {
                Console.WriteLine("The file could not be read:");
                Console.WriteLine(e.Message);
            }
        }

        

    }
}

  