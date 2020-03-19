//Rextester.Program.Main is the entry point for your code. Don't change it.
//Compiler version 4.0.30319.17929 for Microsoft (R) .NET Framework 4.5

using System;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {  // Implicit 
           int a=100;
           float b= a;//no loss of data
           Console.WriteLine(b);
            //explicit
            float c=1010.1010f;
            int d= (int)c;//loss of data
            Console.WriteLine(d);
            
          
        }      
    }
}