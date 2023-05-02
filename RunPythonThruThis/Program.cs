using System;
using System.Diagnostics;

namespace RunPythonFromCS {
    class Program 
    { 
    
        static void Main(string[] args)
        {
            Console.WriteLine("Execute python process...");
            createTuples();
        }

        /*
        static void ExecProcess()
        {
            var psi = new ProcessStartInfo();
            psi.FileName = @"C:\Users\syedr\AppData\Local\Programs\Python\Python311\python.exe";

            var script = @"C:\Users\syedr\OneDrive\Desktop\HackPy\sumTest.py";

            var sum1 = 2;
            var sum2 = 3;

            Console.WriteLine($"{sum1} {sum2}");

            psi.Arguments = $"\"{script}\" \"{sum1}\" \"{sum2}\"";

            Console.WriteLine("Made it thru the args");
            
            psi.UseShellExecute = false;
            psi.CreateNoWindow = true;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;

            var errors = "";
            var results = "";

            using (var process = Process.Start(psi)) 
            {
                errors = process.StandardError.ReadToEnd();
                results = process.StandardOutput.ReadToEnd();
            }

            Console.WriteLine("ERRORS:");
            Console.WriteLine(errors);
            Console.WriteLine("Results:");
            Console.WriteLine(results);
        }
        */
        
        static void createTuples()
        {
            var psi = new ProcessStartInfo();
            psi.FileName = @"C:\Users\syedr\AppData\Local\Programs\Python\Python311\python.exe";

            var script = @"C:\Users\syedr\OneDrive\Desktop\HackPy\tuplesForCS.py";

            Console.WriteLine("Please input the path to the parent: \n");
            var pathToParent = Console.ReadLine();
            Console.WriteLine("and now input the path to the CIP: \n");
            var pathToCIP = Console.ReadLine();

            psi.Arguments = $"\"{script}\" \"{pathToParent}\" \"{pathToCIP}\"";


            psi.UseShellExecute = false;
            psi.CreateNoWindow = true;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;

            var errors = "";
            var results = "";

            using (var process = Process.Start(psi))
            {
                errors = process.StandardError.ReadToEnd();
                results = process.StandardOutput.ReadToEnd();
            }

            Console.WriteLine("ERRORS:");
            Console.WriteLine(errors);
            Console.WriteLine("Results:");
            Console.WriteLine(results);
        }

        

    }


}
