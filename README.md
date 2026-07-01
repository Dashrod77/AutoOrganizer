# AutoOrganizer
Tiempo estimado: 6 - 7 hrs
Autor: Oziel Elias Rodriguez gonzalez
licencia: MIT
Lenguaje: python
plataformas: linux y windows

Problema: Cantidad masiva de archivos de diferentes formatos en una carpeta sin organizacion

Planteamiento: Una cli en python que
1. escanea una carpeta y organiza los archivos que contiene automaticamente en subcarpetas segun su tipo (docuemntos, imagenes, videos, codigos)
2. Mueve archivos segun extension configurable( .pdf, .py, .jpg)
3. genera un reporte de que se realizo cuantos archivos se acomodaron y cuantos errores hubo
4. tendra un modo "undo" que revierte los cambios y estos se guardan en un json con historial
5. funciona exactamente igual para linux como para windows

Caracteristicas principales
Escanea una carpeta y organiza los archivos en subcarpetas por su tipo
Crea un reporte de movimeintos
Modo undo con historial json
Funciona en windows y linux

Requisitos:
-Python 3.10+
-pathlib (stdlib)
-json (stdlib)
-argparse (stdlib)

Instalacion:
git clone
cd AutoOrganizer
git switch dev

Configuracion:
En configuracion se encuentra una lista denominada categorias ahi puedes agregar categorias que no esten disponibles
"mi_categoria": [".ext1", ".ext2"]

Uso:
Ver archivos sin moverlos
python main.py --scan --path "folder"

Organizar los archivos
python main.py --organize --path "folder"

Ver el historial de movimientos
python main.py --history

Deshacer ultimo movimiento
python main.py --undo

Estructura de archivos:
AUTOORGANIZER/
|- Readme.md
|- DESING.md
|- config.json
|- .gitignore
|- main.py
|- organizer/
|   |- __init__.py
|   |- organizer.py
|   |- history.py
|   |- cli.py
