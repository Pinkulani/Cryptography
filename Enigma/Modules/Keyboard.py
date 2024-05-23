class Keyboard:
    def __init__(self, System: str):
        self.System = System
        self.Len = len(self.Sytem)
        self.Text = None

    def Input(self):
        self.Text = str(input("Input: "))

    def Filter(self): # Only keeping Enigma-friendly characters
        Copy = self.Text
        LenCopy = len(Copy)
        self.Text = []

        match self.Len: # Filter by Latin / Swedish or Numerical
            case LatinSwedish if self.Len > 20:
                for TextPosition in range(0, LenCopy):
                    for SystemPosition in range(0, self.Len):
                        if Copy[TextPosition].upper() == self.System[SystemPosition]:
                            self.Text.append(Copy[TextPosition].upper())

            case Numerical if self.Len < 10:
                for TextPosition in range(0, LenCopy):
                    for Number in range(0, self.Len):
                        if Copy[TextPosition] == self.System[Number]: # Only string comparision possible
                            self.Text.append(Copy[TextPosition])

    def ReturnText(self):
        return self.Text
