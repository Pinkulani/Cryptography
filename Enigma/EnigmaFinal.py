import random

# To avoid creating Pointers instead of a new array
def CopyArray(Array):
    Copy = []
    for X in range(0, len(Array)):
        Copy.append(Array[X])

    return Copy

def ShuffleArray(Array):
    random.shuffle(Array)
    return Array


class Rotor:
    def __init__(self):
        self.Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Encryption = ShuffleArray(CopyArray(self.Alpha))

    def Start(self):
        print("Wiring: ", self.Encryption)

A = Rotor()
B = Rotor()
C = Rotor()
A.Start()
B.Start()
C.Start()