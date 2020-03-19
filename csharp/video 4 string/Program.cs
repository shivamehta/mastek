

using System;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
       {
        //escape sequence
        string name = "\"Shivam\"";           
        Console.WriteLine(name);
        string path = "C: \\desktop\\shivam\\DotNet";
        Console.WriteLine(path);
        //new line
        string numbers = "one\ntwo\nthree";
        Console.WriteLine(numbers);
        //verbatim literal
        string path1 = @"C: \desktop\shivam\DotNet";
        Console.WriteLine(path1);
    }
    }
}