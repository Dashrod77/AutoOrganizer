import argparse
from .organizer import FileOrganizer
from pathlib import Path
from .history import History

def main():
  parser = argparse.ArgumentParser(description= "lol")
  parser.add_argument("--scan", action="store_true", help="ver archivos y carpetas sin moverlas")
  parser.add_argument("--undo", action="store_true", help="deshacer el último movimiento")
  parser.add_argument("--history", action="store_true", help="ver el historial de movimientos")
  parser.add_argument("--organize", action="store_true", help="mueve los archivos y carpetas")
  parser.add_argument("--path", default=".", help="ruta del directorio a organizar")
  parser.add_argument("--config", default="config.json", help="ruta del archivo de configuración")
  args = parser.parse_args()

  if args.scan:
    organizer = FileOrganizer(args.config,args.path, ".organizer_history.json")
    organizer.scan()
  elif args.organize:
    organizer = FileOrganizer(args.config,args.path, ".organizer_history.json")
    organizer.scan()
  elif args.undo:
    history = History(".organizer_history.json")
    if history.undo_last_move():
      print("Último movimiento deshecho.")
    else:
      print("No hay movimientos para deshacer.")
  elif args.history:
    history = History(".organizer_history.json")
    if history.moves:
      for move in history.moves:
        print(f"{move['timestamp']}: {move['source']} -> {move['destination']} (categorías: {move['categories']})")
    else:
      print("No hay movimientos en el historial.")
  else:
    parser.print_help()


if __name__ == "__main__":
  main()
