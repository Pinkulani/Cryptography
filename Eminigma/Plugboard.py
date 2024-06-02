class Plugboard:
    def __init__(self, Pairs: str, Converter: object):
        self.Converter = Converter
        self.Wiring = list(self.Converter.System)

        Pairs = Pairs.upper().split()

        for Letter1, Letter2 in Pairs:
            Number1 = self.Converter.LetterToNumber(Letter1)
            Number2 = self.Converter.LetterToNumber(Letter2)

            if self.Wiring[Number1] != Letter1 or self.Wiring[Number2] != Letter2:
                raise ValueError

            self.Wiring[Number1] = Letter2
            self.Wiring[Number2] = Letter1

        self.Wiring = ''.join(self.Wiring) # Convert list to string

    def SignalRight(self, Letter):
        Number = self.Converter.LetterToNumber(Letter)
        return self.Wiring[Number]
    def SignalLeft(self, Input):
        for Number, Letter in enumerate(self.Wiring):
            if Input == Letter:
                return self.Converter.NumberToLetter(Number)
        
