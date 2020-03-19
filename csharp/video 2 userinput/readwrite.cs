using System;


namespace Rextester
{
    class Program
{
        static void Main(string[] args)
    {
        Console.WriteLine("Please enter your name");
        string User_Name = Console.ReadLine();
        Console.WriteLine("Hello {0}", User_Name);
    }
}
}