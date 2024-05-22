class Keyboard:
    def __init__(self):
        self.Text = []
        self.Input()
        self.Filter()

    def Input(self):
        MSG = str(input("Message: "))
        for X in range(0, len(MSG)):
            self.Text.append(MSG[X])

    def Filter(self):
        MSG = self.Text # Clear old text and make space for filtered text
        self.Text = []
        for X in range(0, len(MSG)):
            match MSG[X]: # No special characters
                case " ":
                    continue
                case "ß":
                    continue
                case "ä":
                    continue
                case "ö":
                    continue
                case "ü":
                    continue
                case _:
                    self.Text.append(MSG[X].upper()) # Only Latin script uppercase
    
    def Return(self):
        return self.Text
