from Converter import *
from Data import *
from Keyboard import *
from Lampboard import *
from Rotor import *
from Plugboard import *

class Eminigma:
    def __init__(self):
        print("@ Eminigma \n")
        self.Offset = [0, 0, 0]
        self.SelectModel()
        self.SelectBasics()
        self.SelectRotors()
        self.SelectReflector()
        self.SelectPlugboard()
        self.Run()

    def SelectModel(self):
        Models = list(Data.keys())
        for Number, Model in enumerate(Models):
            print(str(Number + 1) + ".", Model)

        print("")
        while True:
            try:
                Selector = int(input("Choose Model: "))
                if (Selector > len(Models)) or (Selector <= 0):
                    raise ValueError
            except:
                print("Invalid input.")
                continue

            break
        
        self.Model = Data[Models[Selector - 1]]
        print("")

    def SelectBasics(self):
        self.Converter = Converter(self.Model["System"])
        self.Keyboard = Keyboard(self.Model["System"])

    def SelectRotors(self):
        Names = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
        for Number, Wiring in enumerate(self.Model["Rotors"]):
            print(str(Number + 1) + ".", Names[Number], "= Wiring:", Wiring[0], "Turnover: ", Wiring[1])

        print("")
        print("Rotor Input Format: 1 2 3")
        while True:
            try:
                print("Choose Rotors: ", end="")
                Selections = input().split() # Str
                Choices = [] # Int
                for Number in Selections:
                    Choices.append(int(Number))

                for Choice in Choices:
                    if (Choice > len(self.Model["Rotors"])) or (Choice <= 0): # Check too big or too small
                        raise ValueError

                if len(Choices) != len(set(Choices)): # Check using same thing twice
                    raise ValueError

                if len(Choices) != 3: # Check length
                    raise ValueError
                
                Selections = Choices
            except:
                print("Invalid input.")
                continue

            break
        
        print("Chosen Rotors: ", Names[Selections[0] - 1], Names[Selections[1] - 1], Names[Selections[2] - 1], "\n")
        self.Rotor = [0] * 3
        for Number in range(3):
            TMP = self.Model["Rotors"][Selections[Number] - 1]
            self.Rotor[Number] = Rotor(TMP[0], TMP[1], self.Converter, self.Offset[Number])

        # Setup entry Rotor: (not a user choice)
        self.EntryRotor = Rotor(self.Model["Entry"], "", self.Converter, 0, Static=True)

        # Setup extra Rotor
        self.ExtraRotor = None
        if self.Model["Extra"]:
            Names = ["Beta", "Gamma"]
            Wirings = ["LEYJVCNIXWPBQMDRTAKZGFUHOS", "FSOKANUERHMBTIYCWLQPZXVGJD"]

            for Number, Wiring in enumerate(Wirings):
                print(str(Number + 1) + ".", Names[Number], "= Wiring:", Wiring)
            while True:
                try:
                    Selector = int(input("Choose Extra Rotor: "))
                    if (Selector > (len(Names) + 1)) or (Selector <= 0):
                        raise ValueError
                    break
                except:
                    print("Invalid input.")
                    continue
            print("Chosen Extra Rotor: ", Names[Selector-1])
            self.ExtraRotor = Rotor(Wirings[Selector-1], "", self.Converter, 0, Static=True)
            print("")
            

    def SelectReflector(self):
        AmountOfReflectors = len(self.Model["Reflectors"])
        if AmountOfReflectors == 1 and not self.Model["Special"]: # No choice with one Reflector
            TMP = self.Model["Reflectors"][0]
            self.Reflector = Rotor(TMP[0], TMP[1], self.Converter, 0)
        else:
            if AmountOfReflectors == 1 and self.Model["Special"]:
                Names = ["UKW-D"]
            elif AmountOfReflectors == 3:
                Names = ["UKW-A", "UKW-B", "UKW-C", "UKW-D"]
            else:
                if self.Model["Name"] == "Enigma M3":
                    Names = ["UKW-B", "UKW-C", "UKW-D"]
                else:
                    Names = ["UKW-B-Thin", "UKW-C-Thin", "UKW-D"]

            for Number, Reflector in enumerate(self.Model["Reflectors"]):
                print(str(Number + 1) + ".", Names[Number], "= Wiring:", self.Model["Reflectors"][Number][0])

            if len(Names) > len(self.Model["Reflectors"]):
                print(str(len(Names))+". UKW-D \n")

            while True:
                try:
                    Selector = int(input("Choose Reflector: "))
                    if (Selector > (len(Names) + 1)) or (Selector <= 0):
                        raise ValueError
                except:
                    print("Invalid input.")
                    continue

                break

            print("Chosen Reflector: ", Names[Selector - 1])
            if Names[Selector - 1] == "UKW-D":
                while True:
                    try:
                        print("Choose wiring for special UKW-D Reflector.")
                        print("The Letters should be O-B wired together, but don't have to be in this implementation")
                        print("Input format: AC BK")
                        Pairs = input("Enter wiring: ")
                        Pairs = Pairs.upper().split()

                        Wiring = list(self.Model["System"])

                        for Letter1, Letter2 in Pairs:
                            Number1 = self.Converter.LetterToNumber(Letter1)
                            Number2 = self.Converter.LetterToNumber(Letter2)

                            if Wiring[Number1] != Letter1 or Wiring[Number2] != Letter2:
                                raise ValueError

                            Wiring[Number1] = Letter2
                            Wiring[Number2] = Letter1

                        Wiring = ''.join(Wiring) # Convert list to string
                        self.Reflector = Rotor(Wiring, "", self.Converter,  0, Static=True)
                        break
                    except:
                        print("Invalid input.")
            else:
                TMP = self.Model["Reflectors"][Selector - 1]
                self.Reflector = Rotor(TMP[0], TMP[1], self.Converter, 0)
            print("")

    def SelectPlugboard(self):
        if not self.Model["Plugboard"]:
            self.Plugboard = None
            return

        print("Choose Plugboard settings\nInput Format: BC DK")
        while True:
            try:
                print("Choose letters to switch: ", end="")
                Pairs = input()
                self.Plugboard = Plugboard(Pairs, self.Converter)
                break
            except:
                print("Invalid input.")
        print("")

    def Run(self):
        Text = self.Keyboard.Run()

        Message = []
        for Letter in Text:
            # Rotate Rotors
            RotateRotor = [False, False, True] # always rotate last rotor
            RotateReflector = False
            Cogwheel = self.Model["Cogwheel"]

            for Number in [2, 1, 0]:
                if self.Rotor[Number].IsAtTurnover() == True:
                    RotateRotor[Number] = True
                    if not Cogwheel:
                        if Number == 0:
                            RotateReflector = True
                        else:
                            RotateRotor[Number-1] = True
                elif Cogwheel:
                    RotateRotor[Number] = True
                    break

            if RotateReflector and self.Model["Turnable"]:
                self.Reflector.Rotate()
            for Number in [0,1,2]:
                if RotateRotor[Number]:
                    self.Rotor[Number].Rotate()
            
            # Send signal through Rotors
            Letter = self.EntryRotor.SignalRight(Letter)
            if self.Model["Plugboard"]:
                Letter = self.Plugboard.SignalRight(Letter)

            for Number in [2,1,0]:
                Letter = self.Rotor[Number].SignalRight(Letter)
            if self.Model["Extra"]:
                Letter = self.ExtraRotor.SignalRight(Letter)

            Letter = self.Reflector.SignalRight(Letter)

            if self.Model["Extra"]:
                Letter = self.ExtraRotor.SignalLeft(Letter)
            for Number in [0,1,2]:
                Letter = self.Rotor[Number].SignalLeft(Letter)

            if self.Model["Plugboard"]:
                Letter = self.Plugboard.SignalLeft(Letter)
            Letter = self.EntryRotor.SignalLeft(Letter)

            # Append encrypted Letter
            Message.append(Letter)
            
        Lampboard(Message)

if __name__ == "__main__":
    Eminigma = Eminigma()
