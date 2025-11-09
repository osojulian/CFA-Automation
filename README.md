# 🧪 Prueba Técnica — Automatización QA (CFA)

Repositorio: **Automatización de casos de prueba** para la **Cooperativa Financiera de Antioquia (CFA)**  
Tecnologías: **Python 3.11**, **Selenium**, **PyTest**, **pytest-html**, **.NET 9.0**, **PythonNET**

---

## 📌 Resumen del entregable
Este proyecto contiene la definición y automatización (con Selenium + PyTest) de los **5 casos de prueba de aceptación**.  
Se incluyen scripts automatizados, capturas de evidencia y un reporte HTML generado por PyTest.  
Además, se proporciona un **ejecutor .NET** que permite ejecutar las pruebas desde un entorno .NET utilizando PythonNET.

---

## 📂 Estructura del proyecto

```
CFA/
├── __pycache__/
├── .pytest_cache/
├── build/
├── cfa_automation/
│   ├── __pycache__/
│   ├── __init__.py
│   └── runner.py
├── CFA_Automation.egg-info/
├── dist/
├── dotnet_runner/
│   └── CFAExecutor/
│       ├── bin/
│       ├── obj/
│       ├── CFAExecutor.csproj
│       └── Program.cs
├── drivers/
├── evidencias/
├── pages/
│   ├── __pycache__/
│   ├── contact_page.py
│   ├── login_page.py
│   ├── news_page.py
│   ├── simulate_page.py
│   └── verification_page.py
├── test/
│   ├── utils/
│   ├── conftest.py
│   ├── README.md
│   ├── report.html
│   ├── requirements.txt
│   └── setup.py
├── venv/
├── .gitignore
├── conftest.py
├── README.md
├── report.html
├── requirements.txt
└── setup.py
```

---

## 📋 Descripción de Componentes

### 🐍 `cfa_automation/`
Módulo de integración y ejecución.

- **`__init__.py`**: Inicialización del paquete Python
- **`runner.py`**: Script ejecutor principal de las pruebas

---

### 📄 `pages/` - Page Object Model (POM)
Implementación del patrón Page Object en la raíz del proyecto.

- **`contact_page.py`**: Página de contacto y formularios PQRS
- **`login_page.py`**: Página de inicio de sesión (Oficina Virtual)
- **`news_page.py`**: Página de navegación y noticias
- **`simulate_page.py`**: Simulador de crédito
- **`verification_page.py`**: Verificación de secciones principales

---

### 🧪 `test/` - Casos de Prueba
Casos de prueba automatizados con PyTest.

**Archivos de prueba:**
- `test_login.py` - TC01: Inicio de sesión exitoso
- `test_pqrs_form.py` - TC02: Validación de formulario PQRS
- `test_verification.py` - TC03: Navegación entre secciones principales
- `test_simulate.py` - TC04: Simulador de crédito
- `test_news.py` - TC05: Visualización de noticias

**Otros archivos:**
- **`utils/`**: Utilidades auxiliares (capturas, waits, helpers)
- **`conftest.py`**: Fixtures de PyTest específicas del test
- **`README.md`**: Documentación de pruebas
- **`report.html`**: Reporte HTML generado
- **`requirements.txt`**: Dependencias específicas
- **`setup.py`**: Configuración del entorno de pruebas

---

### 🔷 `dotnet_runner/`
Ejecutor de pruebas desarrollado en .NET 9.0 usando PythonNET.

#### 📦 `CFAExecutor/`
- **`Program.cs`**: Punto de entrada que integra Python con .NET
- **`CFAExecutor.csproj`**: Configuración del proyecto .NET
- **`bin/Release/net9.0/`**: Binarios compilados
  - **`CFAExecutor.exe`**: Ejecutable principal (Windows)
  - **`CFAExecutor.dll`**: Biblioteca compilada
  - **`evidencias/report.html`**: Reporte HTML de resultados

---

### 📦 Otros Archivos
- **`drivers/`**: ChromeDriver u otros drivers de Selenium
- **`evidencias/`**: Capturas de pantalla y reportes HTML
- **`venv/`**: Entorno virtual de Python
- **`conftest.py`**: Fixtures de PyTest (configuración del driver)
- **`requirements.txt`**: Dependencias de Python
- **`setup.py`**: Configuración de instalación del paquete
- **`.gitignore`**: Archivos excluidos del control de versiones

---

## ✅ Los 5 Casos de Prueba

### 1) Inicio de sesión exitoso
- **Tipo de prueba:** Aceptación  
- **Prioridad:** Alta  
- **Precondiciones:** El usuario debe tener una cuenta activa en el portal transaccional.  
- **Descripción:** Validar que el sistema permita iniciar sesión correctamente con credenciales válidas en la Oficina Virtual.  
- **Pasos a reproducir:**
  1. Abrir `https://www.cfa.com.co/`.  
  2. Hacer clic en "Ingreso Oficina Virtual".  
  3. Cambiar a la nueva pestaña (`cfavirtual.com.co`).  
  4. Ingresar documento/usuario.  
  5. Presionar continuar.  
  6. (Se carga el teclado virtual—por política no se automatiza la clave).  
- **Resultado esperado:**  
  - Se muestra la pantalla "Ingrese su clave personal. Utilice el teclado virtual".  
  - Flujo hasta carga del teclado sin errores.  
  - *(La redirección al dashboard no se automatiza por seguridad.)*

---

### 2) Validación de formulario de contacto (PQRS)
- **Tipo de prueba:** Aceptación  
- **Prioridad:** Alta  
- **Precondiciones:** Acceso público al sitio.  
- **Descripción:** Verificar que el formulario PQRS funcione correctamente.  
- **Pasos a reproducir:**
  1. Abrir `https://www.cfa.com.co/`.  
  2. Cerrar modal emergente.  
  3. Abrir "Canales de contacto" y seleccionar "PQRS".  
  4. Esperar carga del formulario.  
  5. Seleccionar tipo de solicitud.  
  6. Completar campos obligatorios.  
  7. Presionar **Enviar**.  
- **Resultado esperado:**  
  - Aparece mensaje de confirmación.  
  - Captura de evidencia del envío exitoso.

---

### 3) Navegación entre secciones principales
- **Tipo de prueba:** Aceptación  
- **Prioridad:** Media  
- **Precondiciones:** Página principal accesible.  
- **Descripción:** Verificar que los enlaces del menú redirijan correctamente.  
- **Pasos a reproducir:**
  1. Abrir `https://www.cfa.com.co/`.  
  2. Hacer clic en cada opción del menú (Personas, Empresas, Asociados).  
  3. Verificar carga correcta de cada página.  
- **Resultado esperado:**  
  - Cada enlace carga su sección sin errores.  
  - Capturas de cada sección principales.

---

### 4) Simulador de crédito
- **Tipo de prueba:** Aceptación  
- **Prioridad:** Alta  
- **Precondiciones:** El simulador debe estar disponible.  
- **Descripción:** Verificar que calcule correctamente la cuota según monto y plazo.  
- **Pasos a reproducir:**
  1. Abrir `https://www.cfa.com.co/`.  
  2. Buscar → "Simulador de crédito".  
  3. Ingresar al simulador.
  4. Digitar Monto y Plazo.
  5. Presionar **Calcular**.  
- **Resultado esperado:**  
  - Se muestra cuota estimada, tasa y plazo.  
  - Captura de evidencia con resultado.

---

### 5) Visualización de noticias / boletín (Noticias CFA)
- **Tipo de prueba:** Aceptación  
- **Prioridad:** Media  
- **Precondiciones:** Contenido de noticias publicado.  
- **Descripción:** Validar que la sección "Noticias" cargue correctamente.  
- **Pasos a reproducir:**
  1. Abrir `https://www.cfa.com.co/`.  
  2. Hacer clic en "Noticias".  
  3. Verificar URL `https://www.cfa.com.co/noticias/`.  
  4. Verificar título "Noticias CFA".  
- **Resultado esperado:**  
  - URL contiene `/noticias/`.  
  - Título "Noticias CFA" visible.  
  - Al menos un artículo presente.

---

## 🚀 Instalación y Ejecución

### Requisitos Previos
- **Python 3.11+**
- **.NET 9.0 SDK**
- **Chrome** y **ChromeDriver**
- **PythonNET** (para integración .NET)

---

### 🐍 Configuración Python

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

### 🧩 Generar el .DLL con .NET y PythonNET

#### Configuración en `Program.cs`

```csharp
using Python.Runtime;

class Program
{
    static void Main(string[] args)
    {
        Runtime.PythonDLL = @"C:\Program Files\Python311\python311.dll";
        Environment.SetEnvironmentVariable("PYTHONHOME", @"C:\Users\Julian\Downloads\CFA\venv");
        Environment.SetEnvironmentVariable("PYTHONPATH", @"C:\Users\Julian\Downloads\CFA\venv\Lib\site-packages");

        PythonEngine.Initialize();
        using (Py.GIL())
        {
            dynamic sys = Py.Import("sys");
            sys.path.append(@"C:\Users\Julian\Downloads\CFA");
            dynamic runner = Py.Import("cfa_automation.runner");
            runner.run_tests();
        }
        PythonEngine.Shutdown();
    }
}
```

#### Compilar como DLL

```bash
cd "C:\Users\Julian\Downloads\CFA\dotnet_runner\CFAExecutor"
dotnet build -c Release
```

**Salida:**
```
C:\Users\Julian\Downloads\CFA\dotnet_runner\CFAExecutor\bin\Release\net9.0\CFAExecutor.dll
```

---

### ▶️ Ejecutar Pruebas

#### **Opción 1: Ejecutor Python (PyTest)**
```bash
pytest --html=evidencias/report.html --self-contained-html
```

#### **Opción 2: Ejecutor .NET (modo desarrollo)**
```bash
cd dotnet_runner/CFAExecutor
dotnet run
```

#### **Opción 3: Ejecutable compilado (.DLL)**
```bash
dotnet dotnet_runner/CFAExecutor/bin/Release/net9.0/CFAExecutor.dll
```

#### **Opción 4: Ejecutable (.EXE) - Solo Windows**
```bash
dotnet_runner\CFAExecutor\bin\Release\net9.0\CFAExecutor.exe
```

---

## 📊 Reportes

Los reportes HTML de ejecución se generan automáticamente en:

**Pytest:**
```
evidencias/report.html
```

**.NET Executor:**
```
dotnet_runner/CFAExecutor/bin/Release/net9.0/evidencias/report.html
```

---

## 🔁 Integración CI/CD

Pasos generales para integrar en un pipeline:

1. **Instalar Python 3.11+**
2. **Instalar Chrome y ChromeDriver**
3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar pruebas:**
   ```bash
   pytest --html=evidencias/report.html --self-contained-html
   ```
5. **Publicar reporte como artefacto**

> Para integración con .NET o pipelines, se puede usar el ejecutable DLL generado con **PythonNET**.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.11** - Lenguaje principal de automatización
- **Selenium WebDriver** - Framework de automatización web
- **PyTest** - Framework de testing
- **pytest-html** - Generación de reportes HTML
- **.NET 9.0** - Ejecutor y orquestador de pruebas
- **PythonNET** - Integración Python-C#
- **Page Object Model (POM)** - Patrón de diseño para mantenibilidad

---

## 🧩 Evidencias

- ✅ Capturas automáticas en `evidencias/`
- ✅ Reporte HTML generado por PyTest
- ✅ Logs de ejecución
- ✅ Screenshots de cada caso de prueba

---

## 👨‍💻 Autor

**Julian Andres Osorio Murillo**  
Ingeniero Informático  
📍 Medellín, Colombia

---

## 📄 Licencia

Este proyecto es de uso educativo y técnico para la prueba de automatización QA de CFA.
