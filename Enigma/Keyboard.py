class Keyboard:
    def __init__(self, System: str):
        self.System = System

    def Run(self) -> str:
        return self.Filter(self.Input())

    def Input(self) -> str:
        return str(input("Input: "))

    def Filter(self, Unfiltered: str) -> str: # Only keeping Enigma-friendly characters
        Clean = []
        for Letter in Unfiltered.upper():
            if Letter in self.System:
                Clean.append(Letter)
                        
        return Clean
