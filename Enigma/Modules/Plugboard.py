class Plugboard:
    def __init__(self, System: str):
        self.System = System
        self.Len = len(self.System)
        self.Wiring = []
        self.Text = None

    def ReturnWiring(self):
        return self.Wiring

    def Input(self):
        print("   ", "Plugboard Format: AB DE GL")
        print("   ", "Leave empty for no connections.")
        self.Text = str(input("    Connections: "))
    
    def Filter(self):
        Clean = [] # Filter space
        for Position in range(0, len(self.Text)):
            if self.Text[Position].isalpha() == True:
                Clean.append(self.Text[Position].upper())
        
        Connections = len(Clean)
        match Connections: # Input validation
            case 0:
                print("   ", "No plugboard connections.")
            case Wrong if Connections % 2 != 0:
                print("   ", "Invalid input.")
            case _:
                WireStart = [] # Change letter from start to end position
                WireEnd = []
                for Pair in range(0, Connections, 2): # Format: [[A, B], [D, E], [G, L]]
                    WireStart.append(Clean[Pair])
                    WireEnd.append(Clean[Pair + 1])

                self.Wiring = [0] * self.Len # Expand array to system length and add wiring
                Cables = len(WireStart)
                for ConnectionPosition in range(0, Cables):
                    for SystemPosition in range(0, self.Len):
                        if WireStart[ConnectionPosition] == self.System[SystemPosition]:
                            self.Wiring[SystemPosition] = WireEnd[ConnectionPosition]
                            # Format: [B, 0, 0, E, 0, 0, L, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
