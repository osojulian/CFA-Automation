from setuptools import setup, find_packages

setup(
    name="CFA_Automation",
    version="1.0",
    description="Automatización de pruebas funcionales CFA",
    author="Julian Andrés Osorio Murillo",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "pytest",
        "pytest-html",
        "python-dotenv",
        "pythonnet"
    ],
    entry_points={
        "console_scripts": [
            "run_cfa_tests=cfa_automation.runner:run_tests"
        ]
    }
)

