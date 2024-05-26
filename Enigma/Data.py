class Data:
    def __init__(self, Model: str):
        # Defaults
        self.Cogwheel = False
        self.System = 0
        self.Plugboard = False
        self.ExtraRotor = False
        self.ExtraReflector = False
        self.Entry = None
        self.Reflector = None
        self.Rotors = None

        match Model:
            case "D":
                self.Entry = "ETW-D"
                self.Reflector = "UKW-D"
                self.Rotors = ["I-D", "II-D", "III-D"]
            case "K":
                self.Entry = "ETW-D"
                self.Reflector = "UKW-D"
                self.Rotors = ["I-K", "II-K", "III-K"]
            case "I":
                self.Plugboard = True
                self.Entry = "ETW"
                self.Reflector = "UKW-B"
                # self.ExtraReflector = "UKW-D"
                self.Rotors = ["I", "II", "III"]
            case "M3":
                self.Plugboard = True
                self.Entry = "ETW"
                self.Reflector = "UKW-B"
                # self.ExtraReflector = "UKW-D"
                self.Rotors = ["I", "II", "III"]
            case "M4":
                self.Plugboard = True
                self.ExtraRotor = "Beta"
                self.Entry = "ETW"
                self.Reflector = "UKW-B-Thin"
                # self.ExtraReflector = "UKW-D"
                self.Rotors = ["I", "II", "III"]
            case "A28":
                self.Cogwheel = True
                self.Entry = "ETW-A28"
                self.Reflector = "UKW-A28"
                self.Rotors = ["I-A28", "II-A28", "III-A28"]
            case "G31":
                self.Cogwheel = True
                self.Plugboard = True
                self.Entry = "ETW"
                self.Reflector = "UKW-G31"
                self.Rotors = ["I-G31", "II-G31", "III-G31"]
            case "Z":
                self.Cogwheel = True
                self.System = 2
                self.Entry = "ETW-Z"
                self.Reflector = "UKW-Z"
                self.Rotors = ["I-Z", "II-Z", "III-Z"]
            case "A-133":
                self.System = 1
                self.Entry = "ETW-A-133"
                self.Reflector = "UKW-A-133"
                self.Rotors = ["I-A-133", "II-A-133", "III-A-133"]
            case "T":
                self.Entry = "ETW-T"
                self.Reflector = "UKW-T"
                self.Rotors = ["I-T", "II-T", "III-T"]

    def ReturnSystem(self) -> str:
        match self.System:
            case 0: # Latin
                return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            case 1: # Swedish
                return "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
            case 2: # Numerical
                return "1234567890"
            
    def ReturnExtraRotor(self):
        match self.ExtraRotor:
            case "Beta":
                return "LEYJVCNIXWPBQMDRTAKZGFUHOS"
            case "Gamma":
                return "FSOKANUERHMBTIYCWLQPZXVGJD"
            case False:
                return False
            
    def ReturnExtraReflector(self):
        match self.ExtraReflector:
            case "UKW-D":
                return "A0ZXWVUTSRQPON0MLKIHGFEDCB"
            case False:
                return False
            
    def ReturnEntry(self) -> str:
        match self.Entry:
            case "ETW":
                return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            case "ETW-D":
                return "QWERTZUIOASDFGHJKPYXCVBNML"
            case "ETW-A28":
                return "QWERTZUIOASDFGHJKPYXCVBNML"
            case "ETW-Z":
                return "1234567890"
            case "ETW-A-133":
                return "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
            case "ETW-T":
                return "KZROUQHYAIGBLWVSTDXFPNMCJE"
            
    def ReturnReflector(self):
        match self.Reflector:
            case "UKW-A":
                return ["EJMZALYXVBWFCRQUONTSPIKHGD", False]
            case "UKW-B":
                return ["YRUHQSLDPXNGOKMIEBFZCWVJAT", False]
            case "UKW-C":
                return ["FVPJIAOYEDRZXWGCTKUQSBNMHL", False]
            case "UKW-B-Thin":
                return ["ENKQAUYWJICOPBLMDXZVFTHRGS", False]
            case "UKW-C-Thin":
                return ["RDOBJNTKVEHMLFCWZAXGYIPSUQ", False]
            case "UKW-D":
                return ["IMETCGFRAYSQBZXWLHKDVUPOJN", False]
            case "UKW-A28":
                return ["IMETCGFRAYSQBZXWLHKDVUPOJN", False]
            case "UKW-G31":
                return ["RULQMZJSYGOCETKWDAHNBXPVIF", False]
            case "UKW-Z":
                return ["5079183642", "9"]
            case "UKW-A-133":
                return ["LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY", False]
            case "UKW-T":
                return ["GEKPBTAUMOCNILJDXZYFHWVQSR", False]
            
    def ReturnRotor(self, ID: str) -> str:
        match ID:
            case "I-D":
                return ["LPGSZMHAEOQKVXRFYBUTNICJDW", "Z"]
            case "II-D":
                return ["SLVGBTFXJQOHEWIRZYAMKPCNDU", "Z"]
            case "III-D":
                return ["CJGDPSHKTURAWZXFMYNQOBVLIE", "Z"]
            case "I-K":
                return ["LPGSZMHAEOQKVXRFYBUTNICJDW", "Y"]
            case "II-K":
                return ["SLVGBTFXJQOHEWIRZYAMKPCNDU", "E"]
            case "III-K":
                return ["CJGDPSHKTURAWZXFMYNQOBVLIE", "N"]
            case "I":
                return ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"]
            case "II":
                return ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"]
            case "III":
                return ["BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"]
            case "IV":
                return ["ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"]
            case "V":
                return ["VZBRGITYUPSDNHLXAWMJQOFECK", "Z"]
            case "VI":
                return ["JPGVOUMFYQBENHZRDKASXLICTW", "ZM"]
            case "VII":
                return ["NZJHGRCXMYSWBOUFAIVLPEKQDT", "ZM"]
            case "VIII":
                return ["FKQHTLXOCBJSPDZRAMEWNIUYGV", "ZM"]
            case "I-A28":
                return ["LPGSZMHAEOQKVXRFYBUTNICJDW", "SUVWZABCEFGIKLOPQ"]
            case "II-A28":
                return ["SLVGBTFXJQOHEWIRZYAMKPCNDU", "STVYZACDFGHKMNQ"]
            case "III-A28":
                return ["CJGDPSHKTURAWZXFMYNQOBVLIE", "UWXAEFHKMNR"]
            case "I-G31":
                return ["DMTWSILRUYQNKFEJCAZBPGXOHV", "SUVWZABCEFGIKLOPQ"]
            case "II-G31":
                return ["HQZGPJTMOBLNCIFDYAWVEUSRKX", "STVYZACDFGHKMNQ"]
            case "III-G31":
                return ["UQNTLSZFMREHDPXKIBVYGJCWOA", "UWXAEFHKMNR"]
            case "I-Z":
                return ["6418270359", "9"]
            case "II-Z":
                return ["5841097632", "9"]
            case "III-Z":
                return ["3581620794", "9"]
            case "I-A-133":
                return ["PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA", "Ä"]
            case "II-A-133":
                return ["CHNSYÖADMOTRZXBÄIGÅEKQUPFLVJ", "Ä"]
            case "III-A-133":
                return ["ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL", "Ä"]
            case "I-T":
                return ["KPTYUELOCVGRFQDANJMBSWHZXI", "WZEKQ"]
            case "II-T":
                return ["UPHZLWEQMTDJXCAKSOIGVBYFNR", "WZFLR"]
            case "III-T":
                return ["QUDLYRFEKONVZAXWHMGPJBSICT", "WZEKQ"]
            case "IV-T":
                return ["CIWTBKXNRESPFLYDAGVHQUOJZM", "WZFLR"]
            case "V-T":
                return ["UAXGISNJBVERDYLFZWTPCKOHMQ", "YCFKR"]
            case "VI-T":
                return ["XFUZGALVHCNYSEWQTDMRBKPIOJ", "XEIMQ"]
            case "VII-T":
                return ["BJVFTXPLNAYOZIKWGDQERUCHSM", "YCFKR"]
            case "VIII-T":
                return ["YMTPNZHWKODAJXELUQVGCBISFR", "XEIMQ"]
