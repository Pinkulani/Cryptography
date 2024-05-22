class Lampboard:
    def __init__(self):
        self.Text = []

    def Input(self, Text):
        self.Text = Text

    def Output(self): # Format: AAAAA AAAAA AAAAA
        for X in range(0, len(self.Text)):
            if (X % 5 == 0) and (X != 0):
                print("", self.Text[X], end="")
            else:
                print(self.Text[X], end="")
