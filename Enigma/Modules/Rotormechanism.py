class Reflector:
    def __init__(self, Wiring: str):
        self.Wiring = Wiring

    def Switch(self, Position: int):
        return self.Wiring[Position]
    
class Rotor(Reflector):
    def __init__(self, Wiring: str, Notch: str):
        self.Wiring = Wiring
        self.Notch = Notch
        self.Len = len(self.Wiring) # For Rotation

    def Rotate(self):
        Rotation = []
        for Turn in range(0, self.Len):
            if Turn == 0:
                Rotation.append(self.Wiring[self.Len - 1]) # Append last letter
            else:
                Rotation.append(self.Wiring[Turn - 1]) # Append rest

        self.Wiring = Rotation