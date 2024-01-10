# https://github.com/Pinkulani/Cryptography/tree/main/Enigma
# Emilia @ 10.1.2024
import random

# Translate Letter to Number in Alphabet Order (A = 0, C = 2, Z = 26)
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def LetterToNumber(Letter):
    Letter = Letter.upper() # Enigma has no lowercase
    for X in range(0, len(Alphabet)):
        if Letter == Alphabet[X]:
            return X

def ShuffleArray(Array):
    random.shuffle(Array)
    return Array

# To avoid creating Pointers instead of a new array
def CopyArray(Array):
    Copy = []
    for X in range(0, len(Array)):
        Copy.append(Array[X])

    return Copy
     
class Enigma:
    def __init__(self):
        self.Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Toggle = False # False = Encrypt; True = Decrypt 
        self.Text = "" # Input for encryption or decryption
        self.EncryptedText = ""
        self.Encrypted = [] # Arrays for encryption or decryption
        self.Decrypted = []
        self.Counter1 = 0 # Current Rotation in Rotors for encryption
        self.Counter2 = 0
        self.Counter3 = 0
        self.InverseCounter1 = 0 # Reverse Counter for decryption starting at last letter from encryption
        self.InverseCounter2 = 0
        self.InverseCounter3 = 0
        self.A = ShuffleArray(CopyArray(self.Alphabet)) # Rotors
        self.B = ShuffleArray(CopyArray(self.Alphabet))
        self.C = ShuffleArray(CopyArray(self.Alphabet))
        self.Pointer = 0

    # Revelant Start and End information
    def Start(self):
        print("<- Start ->")
        print("Wiring: ", self.A)
        print("Wiring: ", self.B)
        print("Wiring: ", self.C)

    def End(self):
        print("<- End ->")
        print("Counter 1: ", self.Counter1)
        print("Counter 2: ", self.Counter2)
        print("Counter 2: ", self.Counter3)
    
    # Input / Output
    def TextInput(self, TXT):
        self.Text = str(TXT)

    def TextEncryptedInput(self, TXT):
        self.EncryptedText = str(TXT)

    def TextOutput(self):
        print("Encrypted Text: ", self.Encrypted)
    
    def TextDecryptedOutput(self):
        print("Decrypted Text: ", self.Decrypted)
    
    def Work(self):
        if self.Toggle == False:
            for X in range(0, len(self.Text)): # Encrypt
                match self.Text[X]: # Check invalid characters
                    case "ö":
                        continue
                    case "ä":
                        continue
                    case "ü":
                        continue
                    case "?":
                        continue
                    case "!":
                        continue
                    case ".":
                        continue
                    case ",":
                        continue
                    case "'":
                        continue
                    case " ":
                        continue
                    case _:
                        self.Pointer = LetterToNumber(self.Text[X])
                        self.Encryptor()
                        self.RotateUp()

        else: # Decrypt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            for X in range(300, 0): # Encrypt
                match self.EncryptedText[X]:
                    case "ö":
                        continue
                    case "ä":
                        continue
                    case "ü":
                        continue
                    case "?":
                        continue
                    case "!":
                        continue
                    case ".":
                        continue
                    case ",":
                        continue
                    case "'":
                        continue
                    case " ":
                        continue
                    case _:
                        self.Encryptor()


    def Encryptor(self): # Letter will be translated to be number to route a new letter
        L = self.Pointer # Pointer = Current Letter
        L = self.A[L] # Change Letter with Rotor A
        L = LetterToNumber(L) # Get Letter from Rotor Array and change it to number for next array
        L = self.B[L]
        L = LetterToNumber(L)
        L = self.B[L]
        L = LetterToNumber(L)
        self.Encrypted.append(Alphabet[L])

    def RotateUp(self): # Rotate Rotors
        if self.Counter1 == 26:
            self.Counter1 = 0
            self.Counter2 += 1
            if self.Counter2 == 26:
                self.Counter2 = 0
                self.Counter3 += 1
        else:
            self.Counter1 += 1

# Use of Enigma       
Enigma = Enigma()
Enigma.Start()
print("")

Enigma.TextInput("Hallo, ich kann verschlüsselnnnnnnnnn!")
Enigma.Work()
Enigma.TextOutput()


print("")
Enigma.End()