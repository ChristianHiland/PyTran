from pathlib import Path
import platform
import json
import os

class Start:
  # The Init Func
  def __init__(self):
    self.HomeDIR = Path.cwd()
    self.Username = os.getlogin()
    self.OS = platform.uname()
    self.ConfigFile = str("PyTran/Config.json")
  # First Run
  def First(self):
    Layout = {
      "WorkFolder": self.HomeDIR,
      "Username": self.Username,
      "OS": self.OS
    }
    with open(self.ConfigFile, "w") as Write:
      json.dump(Layout, Write, indent=4)
