def COMPNTS(ID: str) -> bool:
    match ID: # [Cogwheel, Plugboard, Extra Rotor, Extra Reflector, Turnable Reflector]
        case "D":
            return [False, False, False, False, False]
        case "K":
            return [False, False, False, False, False]
        case "I":
            return [False, True, False, True, False]
        case "M3":
            return [False, True, False, True, False]
        case "M4":
            return [False, True, True, True, False]
        case "A28":
            return [True, False, False, False, False]
        case "G31":
            return [True, True, False, False, False]
        case "Z":
            return [True, False, False, False, True]
        case "A-133":
            return [False, False, False, False, False]
        case "T":
            return [False, False, False, False, False]
            
def COMPNTNAMES(ID: str) -> str:
    match ID: # [System, Entry wheel, Reflector, Rotor 1, Rotor 2, Rotor 3, Extra Rotor, Special Reflector]
        case "D":
            return ["Latin", "ETW-D", "UKW-D", ["I-D", "II-D", "III-D"], "None", "None"]
        case "K":
            return ["Latin", "ETW-D", "UKW-D", ["I-K", "II-K", "III-K"], "None", "None"]
        case "I":
            return ["Latin", "ETW", "UKW-B", ["I", "II", "III"], "None", "None"]
        case "M3":
            return ["Latin", "ETW", "None", ["I", "II", "III"], "None", "UKW-Special-D"]
        case "M4":
            return ["Latin", "ETW", "UKW-B-Thin", ["I", "II", "III"], "Beta", "None"]
        case "A28":
            return ["Latin", "ETW-D", "UKW-A28", ["I-A28", "II-A28", "III-A28"], "None", "None"]
        case "G31":
            return ["Latin", "ETW", "UKW-G31", ["I-G31", "II-G31", "III-G31"], "None", "None"]
        case "Z":
            return ["Numerical", "ETW-Z", "UKW-Z", ["I-Z", "II-Z", "III-Z"], "None", "None"]
        case "A-133":
            return ["Swedish", "ETW-A-133", "UKW-A-133", ["I-A-133", "II-A-133", "III-A-133"], "None", "None"]
        case "T":
            return ["Latin", "ETW-T", "UKW-T", ["I-T", "II-T", "III-T"], "None", "None"]
            
def WRNG(IDs: str) -> str:
    # [System, Entry wheel, Reflector, Rotor 1, Rotor 2, Rotor 3, Extra Rotor]
    WRNG = []
    WRNG.append(SYSTM(IDs[0]))
    WRNG.append(NTRY(IDs[1]))
    WRNG.append(REFLCTR(IDs[2]))
    RTRS = []
    for Number in range(3):
        RTRS.append(RTR(IDs[3][Number]))
    WRNG.append(RTRS)
    WRNG.append(RTR(IDs[4]))
    WRNG.append(REFLCTR(IDs[5]))
    return WRNG
        
def SYSTM(ID: str) -> str:
    match ID:
        case "Latin":
            return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        case "Swedish":
            return "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
        case "Numerical":
            return "1234567890"
            
def NTRY(ID: str) -> str:
    match ID:
        case "ETW":
            return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        case "ETW-D":
            return "QWERTZUIOASDFGHJKPYXCVBNML"
        case "ETW-Z":
            return "1234567890"
        case "ETW-A-133":
            return "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
        case "ETW-T":
            return "KZROUQHYAIGBLWVSTDXFPNMCJE"
            
def REFLCTR(ID: str) -> str:
    match ID:
        case "UKW-D":
            return "IMETCGFRAYSQBZXWLHKDVUPOJN"
        case "UKW-A":
            return "EJMZALYXVBWFCRQUONTSPIKHGD"
        case "UKW-B":
            return "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        case "UKW-C":
            return "FVPJIAOYEDRZXWGCTKUQSBNMHL"
        case "UKW-B-Thin":
            return "ENKQAUYWJICOPBLMDXZVFTHRGS"
        case "UKW-C-Thin":
            return "RDOBJNTKVEHMLFCWZAXGYIPSUQ"
        case "UKW-Special-D":
            return "A0ZXWVUTSRQPON0MLKIHGFEDCB"
        case "UKW-A28":
            return "IMETCGFRAYSQBZXWLHKDVUPOJN"
        case "UKW-G31":
            return "RULQMZJSYGOCETKWDAHNBXPVIF"
        case "UKW-Z":
            return ["5079183642", "9"]
        case "UKW-A-133":
            return "LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY"
        case "UKW-T":
            return "GEKPBTAUMOCNILJDXZYFHWVQSR"
        case _:
            return "None"
            
def RTR(ID: str) -> str:
    match ID:
        # Commercial machines
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
        
        # Military machines
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
        case "Beta":
            return "LEYJVCNIXWPBQMDRTAKZGFUHOS"
        case "Gamma":
            return "FSOKANUERHMBTIYCWLQPZXVGJD"
            
        # Cogwheel machines
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
        
        # Special machines
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
        case "VII-T":
            return ["YMTPNZHWKODAJXELUQVGCBISFR", "XEIMQ"]
            
        case _:
            return "None"