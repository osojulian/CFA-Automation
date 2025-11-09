using System;
using Python.Runtime;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            Console.WriteLine("Inicializando entorno Python...");

            // Ruta del runtime de Python 3.11
            Runtime.PythonDLL = @"C:\Users\Julian\AppData\Local\Programs\Python\Python311\python311.dll";

            PythonEngine.Initialize();

            using (Py.GIL())
            {
                Console.WriteLine("Configurando entorno de scripts...");
                
                // 👉 Agregamos la ruta del proyecto principal (donde está cfa_automation)
                dynamic sys = Py.Import("sys");
                sys.path.append(@"C:\Users\Julian\Downloads\CFA");

                Console.WriteLine("Ejecutando pruebas automatizadas CFA...");
                dynamic runner = Py.Import("cfa_automation.runner");
                runner.run_tests();
            }

            PythonEngine.Shutdown();
            Console.WriteLine("✅ Pruebas completadas con éxito.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("❌ Error ejecutando pruebas: " + ex.Message);
            Console.WriteLine(ex.StackTrace);
        }
    }
}
