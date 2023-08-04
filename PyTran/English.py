import json
import os

class English:
    # The Init
    def __init__(self):
        self.JSONFile = str("PyTran/EnglishSen.json")
        self.JSONWhole = str("PyTran/English.json")
        pass
    # The Translate Func
    def Translate(self, Word, Whole):
        if Whole.lower() == str("n"):
            with open(self.JSONFile, "r") as Tran:
                Data = json.load(Tran)
                print(Data['EnglishSen'][Word])
        elif Whole.lower() == str("y"):
            with open(self.JSONWhole, "r") as Tran:
                Data = json.load(Tran)
                print(Data['English'][Word])
    # The Writing Func
    def Write(self, Dict, Whole):
        if Whole.lower() == str("n"):
            with open(self.JSONFile) as Fp:
                Data = json.load(Fp)
                Data.update(Dict)
                with open(self.JSONFile, "r+") as Add:
                    json.dump(Data, Add, indent=4, ensure_ascii=False)
        elif Whole.lower() == str("y"):
            with open(self.JSONWhole) as Fp:
                Data = json.load(Fp)
                Data.update(Dict)
                with open(self.JSONWhole, "r+") as Add:
                    json.dump(Data, Add, indent=4, ensure_ascii=False)
