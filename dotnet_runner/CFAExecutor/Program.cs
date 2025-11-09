using System;
using Python.Runtime;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            Console.WriteLine("=".PadRight(60, '='));
            Console.WriteLine("CFA AUTOMATION - .NET Executor");
            Console.WriteLine("=".PadRight(60, '='));
            Console.WriteLine();

            // Ruta del runtime de Python 3.11 (auto-detección)
            string pythonDll = Path.Combine(
                Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
                "Programs", "Python", "Python311", "python311.dll"
            );

            // Verificar que existe
            if (!File.Exists(pythonDll))
            {
                Console.WriteLine($"No se encontró Python en: {pythonDll}");
                Console.WriteLine("Verifica que Python 3.11 esté instalado");
                Console.WriteLine("Descarga: https://www.python.org/downloads/");
                return;
            }

            Console.WriteLine($"✓ Python encontrado: {pythonDll}");
            Runtime.PythonDLL = pythonDll;

            // Obtener la ruta raíz del proyecto de forma relativa
            string projectRoot = Path.GetFullPath(Path.Combine(
                AppDomain.CurrentDomain.BaseDirectory,
                "..", "..", "..", "..", ".."
            ));

            Console.WriteLine($"Ruta del proyecto: {projectRoot}");
            Console.WriteLine();

            PythonEngine.Initialize();

            using (Py.GIL())
            {
                Console.WriteLine("Configurando entorno de scripts...");

                // Agregamos la ruta del proyecto principal (donde está cfa_automation)
                dynamic sys = Py.Import("sys");
                sys.path.append(projectRoot);

                Console.WriteLine("Ejecutando pruebas automatizadas CFA...");
                Console.WriteLine();

                dynamic runner = Py.Import("cfa_automation.runner");
                runner.run_tests();
            }

            PythonEngine.Shutdown();

            Console.WriteLine();
            Console.WriteLine("=".PadRight(60, '='));
            Console.WriteLine("✓ Ejecución completada exitosamente");
            Console.WriteLine("=".PadRight(60, '='));
        }
        catch (Exception ex)
        {
            Console.WriteLine();
            Console.WriteLine("Error en la ejecución:");
            Console.WriteLine(ex.Message);
            Console.WriteLine();
            Console.WriteLine("Stack trace:");
            Console.WriteLine(ex.StackTrace);
        }
    }
}
