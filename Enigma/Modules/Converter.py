class Converter:
    def __init__(self, System: str):
        self.System = System
        self.Len = len(self.System)

    def LetterToNumber(self, Letter: str): # A -> 0; B -> 1
        for X in range(0, self.Len):
            if Letter == self.System[X]:
                return X # Int
            
    def NumberToLetter(self, Number: int): # 0 -> A; 1 -> B
        return self.System[Number] # String
    
    def LettersToNumbers(self, Letters: str): # ABCDE -> 01234
        Numbers = []
        for X in range(0, len(Letters)):
            Numbers.append(self.LetterToNumber(Letters[X]))
        
        return Numbers # Array : Int
    
    def NumbersToLetters(self, Numbers: int): # 01234 -> ABCDE
        Letters = []
        for X in range(0, len(Numbers)):
            Letters.append(self.NumberToLetter(Numbers[X]))
        
        return Letters # Array : String
