from pathlib import Path
from datetime import datetime
import json


class History:
  def __init__(self, history_file):
    self.history_file = Path(history_file).expanduser()
    self.moves = []
    self.load_history()

  def load_history(self):
    if self.history_file.exists():
      with open(self.history_file) as f:
        self.moves = json.load(f)

  def save_history(self):
    with open(self.history_file, 'w') as f:
      json.dump(self.moves, f, indent=4)

  def log_move(self, source, destination, categories):
    self.moves.append({
      "timestamp": datetime.now().isoformat(),
      "source": str(source),
      "destination": str(destination),
      "categories": categories
    })
    self.save_history()
  def undo_last_move(self):
    if not self.moves:
      return False
    last_move = self.moves.pop()
    self.source = Path(last_move["source"])
    self.destination = Path(last_move["destination"])
    if not self.destination.exists():
      return False
    self.destination.rename(self.source)
    self.save_history()
    return True
