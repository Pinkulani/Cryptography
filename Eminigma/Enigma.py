class Enigma:
    def __init__(self):
        print("@ Eminigma \n")
        self.Select()

    def Select(self):
        Models = ["Enigma I", "Enigma M3", "Enigma M4"]
        Counter = 1
        for Model in Models:
            print(Counter, end="")
            print(".", Model)
            Counter += 1

        print("")
        Selector = int(input("Choose model: "))
        self.Model = Models[Selector - 1]

if __name__ == "__main__":
    Enigma = Enigma()