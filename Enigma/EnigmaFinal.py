# https://github.com/Pinkulani/Cryptography/tree/main/Enigma
# Emilia @ 20.11.2023
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

# Translate Letter to Number in Alphabet Order (A = 0, C = 2)
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def LetterToNumber(Letter):
    Letter = Letter.upper() # Enigma has no lowercase
    for X in range(0, len(Alphabet)):
        if Letter == Alphabet[X]:
            return X

# Enigma
class Enigma:
    def __init__(self):
        self.Text = ""
        self.Encrypted = []
        self.Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Counter = 0 # Current Letter
        self.InverseCounter = 0 # Counter for decryption starting @ last letter from encryption
        # Rotors
        self.A = ShuffleArray(CopyArray(self.Alpha))
        self.B = ShuffleArray(CopyArray(self.Alpha))
        self.C = ShuffleArray(CopyArray(self.Alpha))

    def Start(self):
        print("Wiring: ", self.A)
        print("Wiring: ", self.B)
        print("Wiring: ", self.C)
    
    def TextInput(self, TXT):
        self.Text = str(TXT)

    def Encrypt(self):
        for X in range(0, len(self.Text)):
            match self.Text[X]:
                # Check invalid characters
                case ",":
                    continue
                case "'":
                    continue
                case " ":
                    continue
                case _:
                    self.Encryptor()

    def Encryptor(self): # Letter will be translated to be number to route a new letter
        L = self.Counter # Counter = Current Letter
        # Rotor 1
        L = self.A[L]
        # Rotor 2
        L = LetterToNumber(L)
        L = self.B[L]
        # Rotor 3
        L = LetterToNumber(L)
        L = self.C[L]
        self.Encrypted.append(L)

    def Output(self):
        print("Encrypted Text: ", self.Encrypted)

Enigma = Enigma()
Enigma.Start()
Enigma.TextInput("Hello, I'm a stinky bunny")
Enigma.Output()
