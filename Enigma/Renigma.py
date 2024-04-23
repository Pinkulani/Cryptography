class Rotor:
    def __init__(self):
        self.Counter = 0

    def Reset(self):
        if self.Counter == 26:
            self.Counter = 0

    def Turn(self):
        self.Counter += 1

    def CounterStatus(self):
        return self.Counter
            
class Controller:
    def __init__(self):
        self.Rotor = [0] * 3
        for C in range(0,3):
            self.Rotor[C] = Rotor()

        self.Status()

    def Status(self):
        for C in range(0, 3):
            Rotorvalue = self.Rotor[C].CounterStatus()
            print("Rotor", C, ":", Rotorvalue)


if __name__ == '__main__':
    App = Controller()