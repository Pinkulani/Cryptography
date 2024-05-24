class Keyboard:
    def __init__(self, System: str):
        self.System = System

    def Run(self) -> str:
        Text = self.Input()
        Text = self.Filter(Text) # Only keeping Enigma-friendly characters
        return Text

    def Input(self) -> str:
        return str(input("Input: "))

    def Filter(self, Text: str) -> str:
        LenSystem = len(self.System)
        LenText = len(Text)
        Filtered = []

        # Filter by Latin / Swedish or Numerical
        match LenSystem:
            case LatinSwedish if LenSystem > 20:
                for PositionText in range(LenText):
                    for PositionSystem in range(LenSystem):
                        if Text[PositionText].upper() == self.System[PositionSystem]:
                            Filtered.append(Text[PositionText].upper())

            case Numerical if LenSystem < 10:
                for PositionText in range(0, LenText):
                    for Number in range(0, LenSystem):
                        if Text[PositionText] == self.System[Number]: # Only string comparision possible
                            Filtered.append(Text[PositionText])

        return Filtered
