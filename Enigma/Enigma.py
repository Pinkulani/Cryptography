# https://github.com/Pinkulani/Cryptography/tree/main/Enigma
import random

class Rotor(object):
    def __init__(self):
        self.Name = ""
        self.Letter = "A"
        self.Dictionary = "ABCDEFGHIJKLMOPQRSTUVXYZ"
        self.Encryption = self.Dictionary
        self.Number = 1
    
    def Rename(self, Name):
        self.Name = str(Name)

    def Turn(self):
        self.Number += 1
        self.Letter = self.Dictionary[self.Number]

    def Shuffle(self):
        random.shuffle(self.Encryption)

    def Status(self):
        print("Rotor: ", self.Name)
        print("Letter: ", self.Letter)
        print("Number: ", self.Number)
        print("Original Alphabet: ", self.Dictionary)
        print("(New) Alphabet: ", self.Encryption, "\n")
    
    def Reset(self):
        if self.Number == 26:
            self.Number = 1

# Create Classes
Wheel = []
for Name in ["Wheel1", "Wheel2", "Wheel3"]:
    Object = Rotor()
    Object.Name = Name
    Wheel.append(Object)

# Name
for X in range(len(Wheel)):
    Wheel[X].Rename(X+1)

Wheel[0].Status()
Wheel[1].Status()
Wheel[2].Status()
