import json
import os

class English:
    def __init__(self):
        self.JSONFile = str("PyTran/EnglishSen.json")
        pass
    def Translate(self, Word):
        with open(self.JSONFile, "r") as Tran:
            Data = json.load(Tran)
            print(Data['EnglishSen'][Word])
    def Write(self, Dict):
        with open(self.JSONFile, "w") as Add:
            Data = json.load(Add)
            New = Data.update(Dict)
            json.dump(New, Add, indent=4, ensure_ascii=False)