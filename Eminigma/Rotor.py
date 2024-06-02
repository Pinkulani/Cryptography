class Rotor:
    def __init__(self, Wiring: str, Turnover: str, Converter: object, Offset: int, Static:bool=False):
        self.Wiring = Wiring
        self.Turnover = Turnover
        self.Converter = Converter
        self.Rotation = Offset
        self.Static = Static

        if len(Wiring) != len(Converter.System):
            print("Wiring is incomplete")
            raise ValueError
        SortedWiring = list(Wiring)
        SortedWiring = list(sorted(SortedWiring))

        SortedSystem = list(Converter.System)
        SortedSystem = list(sorted(SortedSystem))

        for i in range(len(SortedWiring)):
            if SortedWiring[i] != SortedSystem[i]:
                print("Using wrong characters")
                raise ValueError

    def Rotate(self):
        if not self.Static:
            self.Rotation += 1 # Turn around at last letter
            if self.Rotation > (len(self.Converter.System) - 1):
                self.Rotation = 0

    def CurrentLetter(self):
        return self.Converter.System[self.Rotation]
    
    def IsAtTurnover(self):
        for Letter in self.Turnover:
            if self.CurrentLetter() == Letter:
                return True
        
        return False
    
    def SignalRight(self, Input): # Wiring on Position of Input
        Index = self.Converter.LetterToNumber(Input) # Int of Position
        Index = Index + self.Rotation # Position + Rotation
        if Index >= len(self.Converter.System): # < Wiring Array
            Index = Index - len(self.Converter.System) # Index - Wiring Array (int)
        
        Letter = self.Wiring[Index]
        Index = self.Converter.LetterToNumber(Letter) # Convert Letter at position to number
        Index = Index - self.Rotation
        if Index < 0:
            Index = Index + len(self.Converter.System)
        return self.Converter.NumberToLetter(Index)
    
    def SignalLeft(self, Input): # Position of Letter in Wiring
        Index = self.Converter.LetterToNumber(Input) # Int of Position
        Index = Index + self.Rotation # Position + Rotation
        if Index >= len(self.Converter.System): # < Wiring Array
            Index = Index - len(self.Converter.System) # Index - Wiring Array (int)
        
        Input = self.Converter.NumberToLetter(Index)
        Match = None
        for Number, Letter in enumerate(self.Wiring):
            if Input == Letter:
                Match = self.Converter.NumberToLetter(Number)
                break

        Index = self.Converter.LetterToNumber(Match) # Convert Letter at position to number
        Index = Index - self.Rotation
        if Index < 0:
            Index = Index + len(self.Converter.System)
        return self.Converter.NumberToLetter(Index)
