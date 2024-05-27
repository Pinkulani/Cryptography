System = {
    "Latin": ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    "Swedish": ("ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"),
    "Numerical": ("1234567890")
}

Entry = {
    "ETW": ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    "ETW-D": ("QWERTZUIOASDFGHJKPYXCVBNML"),
    "ETW-Z": ("1234567890"),
    "ETW-A-133": ("ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"),
    "ETW-T": ("KZROUQHYAIGBLWVSTDXFPNMCJE")
}

Rotor = {
    "I-D": ("LPGSZMHAEOQKVXRFYBUTNICJDW", "Z"),
    "II-D": ("SLVGBTFXJQOHEWIRZYAMKPCNDU", "Z"),
    "III-D": ("CJGDPSHKTURAWZXFMYNQOBVLIE", "Z"),
    "I-K": ("LPGSZMHAEOQKVXRFYBUTNICJDW", "Y"),
    "II-K": ("SLVGBTFXJQOHEWIRZYAMKPCNDU", "E"),
    "III-K": ("CJGDPSHKTURAWZXFMYNQOBVLIE", "N"),
    "I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
    "VI": ("JPGVOUMFYQBENHZRDKASXLICTW", "ZM"),
    "VII": ("NZJHGRCXMYSWBOUFAIVLPEKQDT", "ZM"),
    "VIII": ("FKQHTLXOCBJSPDZRAMEWNIUYGV", "ZM"),
    "I-A28": ("LPGSZMHAEOQKVXRFYBUTNICJDW", "SUVWZABCEFGIKLOPQ"),
    "II-A28": ("SLVGBTFXJQOHEWIRZYAMKPCNDU", "STVYZACDFGHKMNQ"),
    "III-A28": ("CJGDPSHKTURAWZXFMYNQOBVLIE", "UWXAEFHKMNR"),
    "I-G31": ("DMTWSILRUYQNKFEJCAZBPGXOHV", "SUVWZABCEFGIKLOPQ"),
    "II-G31": ("HQZGPJTMOBLNCIFDYAWVEUSRKX", "STVYZACDFGHKMNQ"),
    "III-G31": ("UQNTLSZFMREHDPXKIBVYGJCWOA", "UWXAEFHKMNR"),
    "I-Z": ("6418270359", "9"),
    "II-Z": ("5841097632", "9"),
    "III-Z": ("3581620794", "9"),
    "I-A-133": ("PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA", "Ä"),
    "II-A-133": ("CHNSYÖADMOTRZXBÄIGÅEKQUPFLVJ", "Ä"),
    "III-A-133": ("ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL", "Ä"),
    "I-T": ("KPTYUELOCVGRFQDANJMBSWHZXI", "WZEKQ"),
    "II-T": ("UPHZLWEQMTDJXCAKSOIGVBYFNR", "WZFLR"),
    "III-T": ("QUDLYRFEKONVZAXWHMGPJBSICT", "WZEKQ"),
    "IV-T": ("CIWTBKXNRESPFLYDAGVHQUOJZM", "WZFLR"),
    "V-T": ("UAXGISNJBVERDYLFZWTPCKOHMQ", "YCFKR"),
    "VI-T": ("XFUZGALVHCNYSEWQTDMRBKPIOJ", "XEIMQ"),
    "VII-T": ("BJVFTXPLNAYOZIKWGDQERUCHSM", "YCFKR"),
    "VII-T": ("YMTPNZHWKODAJXELUQVGCBISFR", "XEIMQ")
}

Reflector = {
    "UKW-D": ("IMETCGFRAYSQBZXWLHKDVUPOJN"),
    "UKW-A": ("EJMZALYXVBWFCRQUONTSPIKHGD"),
    "UKW-B": ("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
    "UKW-C": ("FVPJIAOYEDRZXWGCTKUQSBNMHL"),
    "UKW-B-Thin": ("ENKQAUYWJICOPBLMDXZVFTHRGS"),
    "UKW-C-Thin": ("RDOBJNTKVEHMLFCWZAXGYIPSUQ"),
    "UKW-A28": ("IMETCGFRAYSQBZXWLHKDVUPOJN"),
    "UKW-G31": ("RULQMZJSYGOCETKWDAHNBXPVIF"),
    "UKW-Z": ("5079183642", "9"),
    "UKW-A-133": ("LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY"),
    "UKW-T": ("GEKPBTAUMOCNILJDXZYFHWVQSR"),
    "None": ("None")
}

Extra = {
    "Beta": ("LEYJVCNIXWPBQMDRTAKZGFUHOS"),
    "Gamma": ("FSOKANUERHMBTIYCWLQPZXVGJD"),
    "UKW-Special-D": ("A0ZXWVUTSRQPON0MLKIHGFEDCB"),
    "None": ("None")
}

# System, Entry wheel, Reflector, Rotor 1, Rotor 2, Rotor 3, Extra Rotor, Special Reflector
Model = {
    # Commercial machines
    "D": ("Latin", "ETW-D", "UKW-D", ["I-D", "II-D", "III-D"], "None", "None"),
    "K": ("Latin", "ETW-D", "UKW-D", ["I-K", "II-K", "III-K"], "None", "None"),
    # Military machines
    "I": ("Latin", "ETW", "UKW-B", ["I", "II", "III"], "None", "None"),
    "M3": ("Latin", "ETW", "None", ["I", "II", "III"], "None", "UKW-Special-D"),
    "M4": ("Latin", "ETW", "UKW-B-Thin", ["I", "II", "III"], "Beta", "None"),
    # Cogwheel machines
    "A28": ("Latin", "ETW-D", "UKW-A28", ["I-A28", "II-A28", "III-A28"], "None", "None"),
    "G31": ("Latin", "ETW", "UKW-G31", ["I-G31", "II-G31", "III-G31"], "None", "None"),
    "Z": ("Numerical", "ETW-Z", "UKW-Z", ["I-Z", "II-Z", "III-Z"], "None", "None"),
    # Special machines
    "A-133": ("Swedish", "ETW-A-133", "UKW-A-133", ["I-A-133", "II-A-133", "III-A-133"], "None", "None"),
    "T": ("Latin", "ETW-T", "UKW-T", ["I-T", "II-T", "III-T"], "None", "None")
}

class Info:
    def __init__(self, ID: str):
        self.Names = Model[ID]
        self.Wiring = (System[self.Names[0]], Entry[self.Names[1]], Reflector[self.Names[2]], [Rotor[self.Names[3][0]], Rotor[self.Names[3][0]], Rotor[self.Names[3][0]]], Extra[self.Names[4]], Extra[self.Names[5]])
        self.Check(ID)
    
    def Check(self, ID: str) -> bool:
        # Double Step, Turnable Reflector, Plugboard, Extra Rotor, Special Reflector
        Cogwheel = False
        Turnable = False
        Plugboard = False
        Extra = False
        Special = False
        
        if (ID == "A28") or (ID == "G31") or (ID == "Z"):
            Cogwheel = True
        
        if (ID == "I") or (ID == "M3") or (ID == "M4") or (ID == "G31"):
            Plugboard = True

        if (ID == "Z"):
            Turnable = True

        if (ID == "M4"):
            if self.Wiring[4] != "None":
                Extra = True

        if (ID == "I") or (ID == "M3") or (ID == "M4"):
            if self.Wiring[5] != "None":
                Special = True
        
        self.Flags = (Cogwheel, Turnable, Plugboard, Extra, Special)
