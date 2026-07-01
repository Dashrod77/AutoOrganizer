Diagrama de flujo:
START
  |
[Parsear argumentos CLI]
  |
|-> --scan = Mostrar archivos
|-> --organize = Mover archivos + Historial
|-> --undo = Revertir ultimo movimiento
|-> --history = Ver historial
  |
END

Estructura de datos
  Historial.json
    [
      {
        "timestamp": "2026-06-29T15:12:06.480099",   //fecha de la accion
        "source": "/path/to/file.pdf",   //Ruta original del archivo
        "destination": "/path/to/documents/file.pdf",    //Destino del archivo
        "category": "documents"    //Categoria asignada
      }
    ]

config.json
    {
      "categories":
      {
        "docuemnts": [".pdf", ".docx"]
        "categoria": [Tipo de archivo que entra en la categoria]
      }
    }


Desiciones de diseño:
- Se opto usar pathlib para que fuera cross-plataform
- El historial es en json por su simplicidad y portabilidad

Limitaciones conicidas:
- No se manejan archivos sin extension
- No valida conflictos de nombres
- No soporta carpetas anidadas complejas

Mejoras futuras:
- Soporte para archivos sin extension
- Dry-run mode
- Configuracion por linea de comandos
- Logging
