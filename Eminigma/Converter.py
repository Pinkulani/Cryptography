class Converter:
    def __init__(self, System: str):
        self.System = System

    def LetterToNumber(self, Input: str) -> int:
        for Number, Letter in enumerate(self.System):
            if Input == Letter:
                return Number
            
    def NumberToLetter(self, Input: int) -> str:
        return self.System[Input]