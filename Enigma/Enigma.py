from Info import *
from Keyboard import *
from Lampboard import *

class Enigma:
    def __init__(self, Model: str):
        print("@ Enigma", Model)
        self.Setup(Model)
        self.Run()

    def Setup(self, Model: str):
        Data = Info(Model)
        self.Names = Data.Names
        self.Wiring = Data.Wiring
        self.Flags = Data.Flags

        self.Keyboard = Keyboard(self.Wiring[0])
        #self.Rotormechanism = Rotormechanism(self.Wiring, self.Flags)
    
    def Run(self):
        Text = self.Keyboard.Run()

        Lampboard(Text)
        
if __name__ == "__main__":
    Enigma = Enigma("M3")
