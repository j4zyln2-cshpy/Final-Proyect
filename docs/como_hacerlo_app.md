# Forma 1: Descarga PyInstaller, y ejecuta los siguientes comandos:

-- Instalación de pyinstaller: 

pip install pyinstaller:

-- Convertirlo en app ejecutable:

pyinstaller --onefile main.py / 
python -m PyInstaller --onefile main.py

-- (Opcional la verdad) Ocultar la ventana de la consola (yo personalmente no lo haría xd):

pyinstaller --onefile --windowed main.py

-- Añadir icono extra para no tener el de pygame:

pyinstaller --onefile --icon=icono.ico main.py

# Otras librerías a utilizar (desconocía hasta que investigué):

Nuitka: se parece un poco al funciomaiento comúun de un compilador real.

cx_Freeze: por lo que ví, es putil  para crear paquetes e instaladores compatibles con varias versiones recientes de Python.

auto-py-to-exe: una interfaz gráfica basada en PyInstaller que permite hacer ejecutables sin usar la línea de comandos, esta si la conozco más al ser un poco más rápida que pyinstaller 

