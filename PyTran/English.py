import json
import os

class English:
    # The Init
    def __init__(self):
        self.JSONFile = str("PyTran/EnglishSen.json")
        self.JSONWhole = str("PyTran/English.json")
    def Translate(self, Word, Whole):
        """
        This will tranlate English into Korean. If the word is in the dictary!
        Word: The English or Korean word.
        Whole: N will just output the word.
        """
        if Whole.lower() == str("n"):
            with open(self.JSONFile, "r") as Tran:
                Data = json.load(Tran)
                Word = Word.lower()
                return Data[Word]
        elif Whole.lower() == str("y"):
            with open(self.JSONWhole, "r") as Tran:
                Data = json.load(Tran)
                Word = Word.lower()
                return Data[Word]
    def Write(self, Dict, Whole):
        """
        Leting the user add onto the in-build dictanry.
        Y: For the English.json
        N: For the EnglishSen.json
        """
        if Whole.lower() == str("n"):
            with open(self.JSONFile) as Fp:
                Data = json.load(Fp)
                Data.update(Dict)
                with open(self.JSONFile, "r+") as Add:
                    json.dump(Data, Add, indent=4, ensure_ascii=False)
            print("Writing to the JSON was done.")
        elif Whole.lower() == str("y"):
            with open(self.JSONWhole) as Fp:
                Data = json.load(Fp)
                Data.update(Dict)
                with open(self.JSONWhole, "r+") as Add:
                    json.dump(Data, Add, indent=4, ensure_ascii=False)
            print("Writing to the JSON was done.")
