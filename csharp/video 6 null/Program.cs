using System;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
            bool? ismajor = null;
            if (ismajor==true)
            {
                Console.WriteLine("Major");
            }
            else if (ismajor==false)
            {
                Console.WriteLine("Not major");
           
            }
            else 
            {
            Console.WriteLine("User didn't answer");
            }
            
        }      
    }
}