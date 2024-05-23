from Modules.Converter import *
from Modules.Keyboard import *
from Modules.Lampboard import *
from Modules.Plugboard import *
from Modules.Rotormechanism import *
from Data import *

class Enigma:
    def __init__(self):
        self.Debug = True
        self.Settings("I") # Automatically get settings for chosen model
        self.Run()

    def Settings(self, Model: str):
        self.Data = Data(Model)
        self.Name = self.Data.ReturnName()
        self.User = self.Data.ReturnUser()
        self.System = self.Data.ReturnSystem()
        self.PlugboardEnabled = self.Data.ReturnPlugboard()

        # Wiring
        self.Static = self.Data.ReturnStatic()
        self.Reflector = self.Data.ReturnReflector()
        self.Wiring = self.Data.ReturnWiring() # For Rotors
        self.Notches = self.Data.ReturnNotches()
        self.ExtraEnabled = self.Data.ReturnExtra()

        # Info
        self.RotorCount = 3
        self.RotorConnections = len(self.System) # Possible connections for chosen system
        self.Offset = [0] * self.RotorCount # Default Offset: AAA
        self.Text = None
        self.Current = None # Current letter
        self.Previous = None # Previous letter for debugging

        # Create
        self.Keyboard = Keyboard(self.System)
        self.Lampboard = Lampboard()

        if self.RotorConnections > 20: # Numerical doesn't need conversion
            self.Converter = Converter(self.System)

        if self.PlugboardEnabled == True:
            self.Plugboard = Plugboard(self.System)

        if self.ExtraEnabled != None: # Enigma M4
            self.Extra = Reflector(self.Extra)
            self.ExtraEnabled = True

        self.Static = Reflector(self.Static)
        self.Reflector = Reflector(self.Reflector)

        self.Rotor = [0] * self.RotorCount
        for Number in range(self.RotorCount):
            self.Rotor[Number] = Rotor(self.Wiring[Number], self.Notches[Number])

    def Start(self):
        print("Model:", self.Name)
        print("   ", "User:", self.User)
        print("   ", "Specifications in config file")

    def Run(self):
        self.Start()
        # Input
        self.Keyboard.Input()
        self.Keyboard.Filter()
        self.Text = self.Keyboard.ReturnText()
        if self.PlugboardEnabled == True:
            self.Plugboard.Input()
            self.Plugboard.Filter()
            Connections = self.Plugboard.ReturnWiring()
            self.Plugboard = Reflector(Connections)

        # Output
        self.Lampboard.Input(self.Text)
        self.Lampboard.Output()

if __name__ == "__main__":
    App = Enigma()
