class Converter:
    def __init__(self):
        self.Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def Letter(self, Number):
        return self.Alphabet[Number]
    
    def Number(self, Letter):
        for X in range(0, len(self.Alphabet)):
            if Letter == self.Alphabet[X]:
                return X