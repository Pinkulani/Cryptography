class Converter:
    def __init__(self):
        self.Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def Letter(self, Number):
        Text = []
        for X in range(0, len(Number)):
            Text.append(self.Alphabet[Number[X]])

        return Text
    
    def Number(self, Letter):
        Text = []
        for X in range(0, len(Letter)):
            for Y in range(0, len(self.Alphabet)):
                if Letter[X] == self.Alphabet[Y]:
                    Text.append(Y)

        return Text
