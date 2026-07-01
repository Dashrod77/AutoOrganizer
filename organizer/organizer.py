from pathlib import Path
from .history import History
import json

class FileOrganizer:
  def __init__(self, config_path, source_folder, history_file):
    with open(config_path, 'r') as f:
      self.categorias = json.load(f)
    self.source_folder = Path(source_folder).expanduser()
    self.history = History(history_file)
    if not self.source_folder.exists():
      raise FileNotFoundError(f"carpeta no encontrada: {self.source_folder}")

  def scan(self):
    for file in self.source_folder.iterdir():
      if not file.is_file():
        continue
      extension = file.suffix.lower()
      for categories, extensions_list in self.categorias["categories"].items():
        if extension in extensions_list:
          self.organize(file, categories)
          break

  def organize(self, file, categories):
        destination_folder = self.source_folder / categories
        destination_folder.mkdir(exist_ok=True)
        destination_file = destination_folder / file.name
        self.history.log_move(str(file), str(destination_file), categories)
        file.rename(destination_file)
        print(f"Archivo {file.name} movido a {destination_folder}")
  pass
