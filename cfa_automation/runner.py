import pytest
import os

def run_tests():
    # Cambiamos el directorio a la raíz del proyecto CFA
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.chdir(project_root)

    print(f"Ejecutando pytest desde: {os.getcwd()}")

    # Ejecutamos pytest apuntando al directorio correcto
    pytest.main([
        "test",                      # ruta donde están tus casos
        "--html=evidencias/report.html",
        "--self-contained-html"
    ])
