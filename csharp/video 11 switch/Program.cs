using System;
namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
           /* Console.WriteLine("PLease enter a number");
            int a = int.Parse(Console.ReadLine()); */
            int a =30;
           switch(a)
           {
             case 10:
               case 20:
               case 30:
               case 40:
               Console.WriteLine("Its {0}", a);
               break;
               default:
                Console.WriteLine("Not matching");
               break;
            
        }
    }
   
}
}