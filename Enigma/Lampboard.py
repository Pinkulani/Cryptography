class Lampboard:
    def __init__(self):
        self.Text = None

    def Input(self, Text: str):
        self.Text = Text

    def Output(self): # Output Format: AAAAA AAAAA AAAAA
        print("Output: ", end="")
        for Space in range(0, len(self.Text)):
            if (Space % 5 == 0) and (Space != 0):
                print("", self.Text[Space], end="")
            else:
                print(self.Text[Space], end="")