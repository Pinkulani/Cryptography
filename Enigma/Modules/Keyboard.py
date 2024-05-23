class Keyboard:
    def __init__(self, System):
        self.System = System
        self.Input()
        self.Filter()

    def Input(self): # Unfiltered
        self.Text = str(input("Input: "))

    def Filter(self): # Only keeping Enigma-friendly characters
        Copy = self.Text
        self.Text = []
        Len = len(self.System)
        if Len > 20: # Latin / Swedish
            for X in range(0, len(Copy)):
                for Y in range(0, Len):
                    if Copy[X].upper() == self.System[Y]:
                        self.Text.append(Copy[X].upper())
        else: # Numerical
            for Z in range(0, len(Copy)):
                for L in range(0, Len):
                    if Copy[Z] == self.System[L]:
                        self.Text.append(Copy[Z])
    
    def ReturnText(self):
        return self.Text