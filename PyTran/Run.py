import os
from pathlib import Path

class Start:
  # The Init Func
  def __init__(self):
    self.HomeDIR = Path.cwd()
    self.ConfigFile = str("PyTran/")
