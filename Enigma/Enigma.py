from Modules.Converter import *
from Modules.Keyboard import *
from Modules.Lampboard import *
from Modules.Plugboard import *
from Modules.Rotor import *
from Data import *

class Enigma:
    def __init__(self):
        self.Settings("I")
        self.Debug = True

    def Settings(self, Model):
        match Model:
            case "I":
                Static = 0
                System = 0
                Rotors = ["I", "II", "III"]
                Reflector = "B"
            case "M3":
                Static = 0
                System = 0
                Rotors = ["VI", "VII", "VIII"]
                Reflector = "B"
            case "M4":
                Static = 0
                System = 0
                Rotors = ["VI", "VII", "VIII"]
                Extra = "Beta"
                Reflector = "B-M4"

        if Model == "M4":
            self.Data = Data(Static, System, Rotors, Reflector, Extra)
        else:
            self.Data = Data(Static, System, Rotors, Reflector)

        self.Setup()
    
    def Setup(self):
        self.Static = self.Data.ReturnStatic()
        self.System = self.Data.ReturnSystem()
        self.Wiring = self.Data.ReturnWiring()
        self.Notches = self.Data.ReturnNotches()
        self.Reflector = self.Data.ReturnReflector()
        self.Extra = self.Data.ReturnExtra()

        self.Converter = Converter(self.System)
        self.Lampboard = Lampboard()
        self.Keyboard = Keyboard(self.System)
        self.Text = self.Keyboard.ReturnText() # Filtered Text
        self.Plugboard = Plugboard(self.System)

        self.RotorCount = len(self.Wiring) # Amount of Rotors
        self.RotorConnections = len(self.Wiring[0]) # Amount of connections per Rotor
        self.Rotors = [0] * self.RotorCount
        for X in range(0, self.RotorCount):
            self.Rotors[X] = Rotor(self.Converter.LettersToNumbers(self.Wiring[X]), self.Converter.LettersToNumbers(self.Notches[X]))

        self.Offset = [0] * self.RotorCount # Default Offset: AAA
        self.Current = None # Current Letter
        self.Previous = None # Previous Letter for debugging

        self.Table()

    def Rotormechanism(self):
        Copy = self.Text
        self.Text = [] # Final Text
        for X in range(0, len(Copy)):
            self.Current = Copy[X]

    def Table(self): # Print debug info
        if self.Extra != None:
            TableLen = self.RotorCount + 3 # Enigma M4
        else:
            TableLen = self.RotorCount + 2

        # Heading
        for K in range(0, TableLen + 1): # Numbers + Static + Amount of Rotors + Reflector + Extra
            match K:
                case 0: # Numbers
                    print("Numbers", end=" | ")
                case 1:
                    print("Static", end=" | ")
                case Reflector if K == TableLen: # Last column
                    print("Reflector")
                case _:
                    print("Rotor", K-1, end=" | ")
        
        # Content
        for M in range(0, self.RotorConnections): # Numbers + Wiring -> Static -> Rotors -> Reflector -> Extra
            for S in range(0, TableLen):
                match S:
                    case 0: # First column
                        match M:
                            case SMALL if (M >= 0) and (M < 10): 
                                print(M, end=" | ") # Space for single digit numbers
                            case _:
                                print(M, end=" | ") # Space for double digit numbers
                    case 1:
                        print(self.Static[M], end=" | ")
                    case End if S == TableLen: # Reflector
                        print(self.Reflector[M])
                    case _:
                        print(self.Wiring[S-2][M], end=" | ")

            print("")



if __name__ == "__main__":
    App = Enigma()
