from pathlib import Path
from PyTran import Version, Release
import platform
import json
import os

class Start:
  # The Init Func
  def __init__(self):
    self.HomeDIR = Path.cwd()
    self.OS = platform.system()
    self.PyVer = platform.python_version()
    self.ConfigFile = str("PyTran/Config.json")
    if os.path.exists(self.ConfigFile) == False:
      self.First()
    else:
      pass
  # First Run
  def First(self):
    Layout = {
      "System": {
        "WorkFolder": str(self.HomeDIR),
        "OS": str(self.OS),
        "PythonVer": self.PyVer
      },
      "PyTran": {
        "Version": Version,
        "Release": Release
      }
    }
    if os.path.exists(self.ConfigFile) == False:
      with open(self.ConfigFile, "w") as Write:
        json.dump(Layout, Write, indent=4, ensure_ascii=False)
      print("The Config File has been made!")
    else:
      print("Error: Sorry you aready ran the First command!")
    # Returns The Contents of the config file.
  def Info(self):
      print("Do you want the 'System'? Do you want 'PyTran'?")
      OP = input("PyTran/System: ")
      if os.path.exists(self.ConfigFile) == True:
        with open(self.ConfigFile, "r") as Read:
          Data = json.load(Read)
          print(Data[OP])
      else:
        print("Sorry, You don't have a Config file for PyTran")
