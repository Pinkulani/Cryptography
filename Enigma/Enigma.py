from Modules.Converter import *
from Modules.Keyboard import *
from Modules.Lampboard import *
from Modules.Plugboard import *
from Modules.Rotormechanism import *
from Data import *

class Enigma:
    def __init__(self):
        self.Debug = True
        self.Settings("A-133") # Automatically start with settings of chosen model
        self.Start()

    def Settings(self, Model: str):
        Info = Data(Model)
        self.Name = Info.ReturnName()
        self.User = Info.ReturnUser()
        self.System = Info.ReturnSystem()
        self.Plugboard = Info.ReturnPlugboard()

        # Wiring
        self.Static = Info.ReturnStatic()
        self.Reflector = Info.ReturnReflector()
        self.Wiring = Info.ReturnWiring() # For Rotors
        self.Notches = Info.ReturnNotches()
        self.Extra = Info.ReturnExtra() # Enigma M4 Extra-Rotor

        # Info
        self.Connections = len(self.System) # Possible connections for chosen system
        self.Offset = [0] * 3 # Default Offset: [0, 0, 0]
        self.Text = None
        self.Current = None # Current letter
        self.Previous = None # Previous letter for debugging

    def Start(self):
        self.Keyboard = Keyboard(self.System)
        self.Lampboard = Lampboard()
        self.Static = Reflector(self.Static) # Same functionality as Reflector
        self.Reflector = Reflector(self.Reflector)

        if self.Connections > 20: # Numerical doesn't need conversion
            self.Converter = Converter(self.System)

        self.Rotor = [0] * 3
        for Number in range(0, 3): # 3 Rotors
            self.Rotor[Number] = Rotor(self.Wiring[Number], self.Notches[Number])

        Option = -1
        match Option:
            case M4 if (self.Plugboard == True) and (self.Extra != None): # Enigma M4
                Option = 2
            case PG if (self.Plugboard == True) and (self.Extra == None): # Plugboard
                Option = 1
            case Any if (self.Plugboard == False) and (self.Extra == None): # No plugboard
                Option = 0

        self.Run(Option)

    def Info(self):
        print(self.Name)
        print(" User:", self.User)
        if self.Debug == True: # Will print a table with the wiring of every Rotor
            print("")
            for K in range(0, 4): # Heading
                match K:
                    case 0: # Numbers
                        print("Numbers", end=" | ")
                    case End if K == 3: # Last column
                        print("Rotor", K)
                    case _:
                        print("Rotor", K, end=" | ")
        
            for M in range(0, self.Connections): # Content
                for S in range(0, 4):
                    match S:
                        case 0: # Numbers
                            match M:
                                case SMALL if (M >= 0) and (M < 10): 
                                    print(M, end="       | ") # Space for single digit numbers
                                case _:
                                    print(M, end="      | ") # Space for double digit numbers
                        case End if S == 3: # Last column
                                    print(self.Wiring[S-1][M])
                        case _:
                            print(self.Wiring[S-1][M], end="       | ")

            print("")

    def PlugboardRun(self): # # Same functionality as Reflector
        self.Plugboard = Plugboard()
        self.Plugboard.Input()
        self.Plugboard.Filter()
        Wiring = self.Plugboard.ReturnWiring()
        self.Plugboard = Reflector(Wiring) 

    def KeyboardRun(self):
        self.Keyboard.Input()
        self.Keyboard.Filter()
        self.Text = self.Keyboard.ReturnText()

    def Run(self, Option: int):
        self.Info()
        self.KeyboardRun()
        match Option:
            case 2: # M4
                self.PlugboardRun()
            case 1: # I
                self.PlugboardRun()
            case 0: # G
                print("G")

        self.End()
    
    def End(self):
        self.Lampboard.Input(self.Text)
        self.Lampboard.Output()

if __name__ == "__main__":
    App = Enigma()
