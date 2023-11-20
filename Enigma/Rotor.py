class Rotor:
    def __init__(self, Len):
        self.A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Counter = 0
        self.Len = Len
        self.Space = 0
        self.Output = []

    def CheckCounter(self):
        if self.Counter == 26:
            self.Counter = 0

    def CheckSpace(self):
        self.Space = 0

    def Print(self):
        for X in range(0, self.Len):
            if self.Space == 5:
                self.Output.append("&")
                self.CheckSpace()

            self.Output.append(self.A[self.Counter])
            self.Counter += 1
            self.Space += 1
            self.CheckCounter()

        print(self.Output)

Rotor = Rotor(100)
Rotor.Print()