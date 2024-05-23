class Plugboard:
    def __init__(self, System):
        self.System = System
        self.Wiring = [] # Final Wiring
        self.Text = None # Unfiltered Input
        self.Input()
        self.Filter()

    def Input(self):
        print("Plugboard Format: AB DE GL")
        self.Text = input("Connections: ")
    
    def Filter(self):
        NoSpace = [] # Filter out space
        for X in range(0, len(self.Text)):
            if self.Text[X].isalpha() == True:
                NoSpace.append(self.Text[X].upper())

        if len(NoSpace) % 2 == 0: # Look for pairs
            Connections = [] # Paired connections
            for Y in range(0, len(NoSpace), 2):
                Array = [NoSpace[Y], NoSpace[Y+1]]
                Connections.append(Array) # Format: [[A, B], [D, E], [G, L]]
        else:
            print("Faulty input, skipping plugboard connections.") # Error

        WireStart = [] # Change Letter from Start to End
        WireEnd = []
        for G in range(0, len(Connections)):
            WireStart.append(Connections[G][0])
            WireEnd.append(Connections[G][1])

        TotalLetters = len(self.System)
        self.Wiring = [0] * TotalLetters # Expand array and add existing wiring
        for U in range(0, len(Connections)):
            for H in range(0, TotalLetters):
                if WireStart[U] == self.System[H]:
                    self.Wiring[H] = WireEnd[U] # Format: [B, 0, 0, E, 0, 0, L, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def Switch(self, Letter):
        if self.Wiring[Letter] == 0: # 
            return Letter
        else:
            return self.Wiring[Letter]