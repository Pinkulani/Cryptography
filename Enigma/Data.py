class Data:
    def __init__(self, Static, System, Rotors, Reflector, Extra = None):
        self.Static = self.Static(Static)
        self.System = self.System(System)
        self.Wiring = []
        self.Notches = []
        for X in range(0, len(Rotors)):
            self.Wiring.append(self.Rotor(Rotors[X]))
            self.Notches.append(self.Notch(Rotors[X]))
        self.Reflector = self.Reflector(Reflector)
        self.Extra = self.Rotor(Extra)

    def ReturnAlphabet(self):
        return self.Alphabet

    def System(self, Number):
        match Number:
            case 0: # Latin
                return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            case 1: # Swedish
                return "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
            case 2: # Numerical
                return "1234567890"
            
    def Static(self, Number):
        match Number:
            case 0: # Standard
                return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def Rotor(self, Name):
        match Name:
            case "I":
                return "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            case "II":
                return "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            case "III":
                return "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            case "IV":
                return "ESOVPZJAYQUIRHXLNFTGKDCMWB"
            case "V":
                return "VZBRGITYUPSDNHLXAWMJQOFECK"
            case "VI":
                return "JPGVOUMFYQBENHZRDKASXLICTW"
            case "VII":
                return "NZJHGRCXMYSWBOUFAIVLPEKQDT"
            case "VIII":
                return "FKQHTLXOCBJSPDZRAMEWNIUYGV"
            case "Beta":
                return "LEYJVCNIXWPBQMDRTAKZGFUHOS"
            case "Gamma":
                return "FSOKANUERHMBTIYCWLQPZXVGJD"
            
    def Notch(self, Name):
        match Name:
            case "I":
                return "Y"
            case "II":
                return "M"
            case "III":
                return "D"
            case "IV":
                return "R"
            case "V":
                return "H"
            case "VI":
                return "HU"
            case "VII":
                return "HU"
            case "VIII":
                return "HU"
    
    def Reflector(self, Name):
        match Name:
            case "A":
                return "EJMZALYXVBWFCRQUONTSPIKHGD"
            case "B":
                return "YRUHQSLDPXNGOKMIEBFZCWVJAT"
            case "C":
                return "FVPJIAOYEDRZXWGCTKUQSBNMHL"
            case "B-M4":
                return "ENKQAUYWJICOPBLMDXZVFTHRGS"
            case "C-M4":
                return "RDOBJNTKVEHMLFCWZAXGYIPSUQ"