class Data:
    def __init__(self, Model: str):
        self.Setup(Model)
    
    def Setup(self, ID: str):
        match ID:
            case "A-133":
                Name = "Enigma A-133"
                User = "Swedish SGS"
                System = 1
                Plugboard = False
                Static = "ETW-A-133"
                Reflector = "UKW-A-133"
                Rotors = ["I-A-133", "II-A-133", "III-A-133"]
                Extra = None
            case "D":
                Name = "Enigma D"
                User = "Commercial"
                System = 0
                Plugboard = False
                Static = "ETW-D"
                Reflector = "UKW-D"
                Rotors = ["I-D", "II-D", "III-D"]
                Extra = None
            case "I":
                Name = "Enigma I"
                User = "German Army & Air Force"
                System = 0
                Plugboard = True
                Static = "ETW"
                Reflector = "UKW-B"
                Rotors = ["I", "II", "III"]
                Extra = None
            case "M3":
                Name = "Enigma M3"
                User = "German Navy"
                System = 0
                Plugboard = True
                Static = "ETW"
                Reflector = "UKW-B"
                Rotors = ["VI", "VII", "VIII"]
                Extra = None
            case "M4":
                Name = "Enigma M4"
                User = "German Navy"
                System = 0
                Plugboard = True
                Static = "ETW"
                Reflector = "UKW-B-M4"
                Rotors = ["VI", "VII", "VIII"]
                Extra = "Beta" # Enigma M4 exclusive
            case "G":
                Name = "Enigma G"
                User = "Commercial"
                System = 0
                Plugboard = False
                Static = "ETW-D"
                Reflector = "UKW-D"
                Rotors = ["I-G", "II-G", "III-G"]
                Extra = None
            case "T":
                Name = "Enigma T"
                User = "Japanese Army"
                System = 0
                Plugboard = False
                Static = "ETW-T"
                Reflector = "UKW-T"
                Rotors = ["I-T", "II-T", "III-T"]
                Extra = None
            case "Z":
                Name = "Enigma Z"
                User = "Various"
                System = 2
                Plugboard = False
                Static = "ETW-Z"
                Reflector = "UKW-Z"
                Rotors = ["I-Z", "II-Z", "III-Z"]
                Extra = None
        
        self.Info(Name, User, System, Plugboard, Static, Reflector, Rotors, Extra)

    def Info(self, Name: str, User: str, System: int, Plugboard: bool, Static: str, Reflector: str, Rotors: str, Extra: str):
        self.Name = Name
        self.User = User
        self.System = self.System(System)
        self.Plugboard = Plugboard
        self.Static = self.Static(Static)
        self.Reflector = self.Reflector(Reflector)
        self.Wiring = []
        self.Notches = []
        for Number in range(0, 3):
            self.Wiring.append(self.Rotor(Rotors[Number]))
            self.Notches.append(self.Notch(Rotors[Number]))
        self.Extra = self.Rotor(Extra)

    def ReturnName(self):
        return self.Name
    
    def ReturnUser(self):
        return self.User
    
    def ReturnSystem(self):
        return self.System
    
    def ReturnPlugboard(self):
        return self.Plugboard
    
    def ReturnStatic(self):
        return self.Static
    
    def ReturnReflector(self):
        return self.Reflector
    
    def ReturnWiring(self):
        return self.Wiring
    
    def ReturnNotches(self):
        return self.Notches
    
    def ReturnExtra(self):
        return self.Extra
    
    def System(self, ID: int):
        match ID:
            case 0: # Latin
                return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            case 1: # Swedish
                return "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
            case 2: # Numerical
                return "1234567890"

    def Static(self, ID: str):
        match ID:
            case "ETW":
                return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            case "ETW-A-133":
                return "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
            case "ETW-D":
                return "QWERTZUIOASDFGHJKPYXCVBNML"
            case "ETW-T":
                return "KZROUQHYAIGBLWVSTDXFPNMCJE"
            case "ETW-Z":
                return "1234567890"

    def Reflector(self, ID: str):
        match ID:
            case "UKW-A-133":
                return "LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY"
            case "UKW-D":
                return "IMETCGFRAYSQBZXWLHKDVUPOJN"
            case "UKW-A":
                return "EJMZALYXVBWFCRQUONTSPIKHGD"
            case "UKW-B":
                return "YRUHQSLDPXNGOKMIEBFZCWVJAT"
            case "UKW-C":
                return "FVPJIAOYEDRZXWGCTKUQSBNMHL"
            case "UKW-B-M4":
                return "ENKQAUYWJICOPBLMDXZVFTHRGS"
            case "UKW-C-M4":
                return "RDOBJNTKVEHMLFCWZAXGYIPSUQ"
            case "UKW-T":
                return "GEKPBTAUMOCNILJDXZYFHWVQSR"
            case "UKW-Z":
                return "5079183642"
    
    def Rotor(self, ID: str):
        match ID:
            case "I-A-133":
                return "PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA"
            case "II-A-133":
                return "CHNSYÖADMOTRZXBÄIGÅEKQUPFLVJ"
            case "III-A-133":
                return "ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL"
            case "I-D":
                return "LPGSZMHAEOQKVXRFYBUTNICJDW"
            case "II-D":
                return "SLVGBTFXJQOHEWIRZYAMKPCNDU"
            case "III-D":
                return "CJGDPSHKTURAWZXFMYNQOBVLIE"
            case "I-G":
                return "LPGSZMHAEOQKVXRFYBUTNICJDW"
            case "II-G":
                return "SLVGBTFXJQOHEWIRZYAMKPCNDU"
            case "III-G":
                return "CJGDPSHKTURAWZXFMYNQOBVLIE"
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
            case "I-T":
                return "KPTYUELOCVGRFQDANJMBSWHZXI"
            case "II-T":
                return "UPHZLWEQMTDJXCAKSOIGVBYFNR"
            case "III-T":
                return "QUDLYRFEKONVZAXWHMGPJBSICT"
            case "IV-T":
                return "CIWTBKXNRESPFLYDAGVHQUOJZM"
            case "V-T":
                return "UAXGISNJBVERDYLFZWTPCKOHMQ"
            case "VI-T":
                return "XFUZGALVHCNYSEWQTDMRBKPIOJ"
            case "VII-T":
                return "BJVFTXPLNAYOZIKWGDQERUCHSM"
            case "VIII-T":
                return "YMTPNZHWKODAJXELUQVGCBISFR"
            case "I-Z":
                return "6418270359"
            case "II-Z":
                return "5841097632"
            case "III-Z":
                return "3581620794"
            case "Beta":
                return "LEYJVCNIXWPBQMDRTAKZGFUHOS"
            case "Gamma":
                return "FSOKANUERHMBTIYCWLQPZXVGJD"
            
    def Notch(self, ID: str):
        match ID:
            case "I-A-133":
                return "G"
            case "II-A-133":
                return "G"
            case "III-A-133":
                return "G"
            case "I-D":
                return "G"
            case "II-D":
                return "M"
            case "III-D":
                return "V"
            case "I-G":
                return "ACDEHIJKMNOQSTWXY"
            case "II-G":
                return "ABDGHIKLNOPSUVY"
            case "III-G":
                return "CEFIMNPSUVZ"
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
            case "I-T":
                return "EHMSY"
            case "II-T":
                return "EHNTZ"
            case "III-T":
                return "EHMSY"
            case "IV-T":
                return "EHNTZ"
            case "V-T":
                return "GKNSZ"
            case "VI-T":
                return "FMQUY"
            case "VII-T":
                return "GKNSZ"
            case "VIII-T":
                return "FMQUY"
            case "I-Z":
                return "2"
            case "II-Z":
                return "2"
            case "III-Z":
                return "2"
