def Lampboard(Text: str): # Output Format: AAAAA AAAAA AAAAA
    print("Output: ", end="")
    for Space in range(len(Text)):
        if (Space % 5 == 0) and (Space != 0):
            print("", Text[Space], end="")
        else:
            print(Text[Space], end="")

    print("")