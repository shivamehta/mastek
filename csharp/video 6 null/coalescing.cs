using System;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int? a = 100;
            int b= a ?? 0;
            Console.WriteLine("{0}",b);
          
        }      
    }
}