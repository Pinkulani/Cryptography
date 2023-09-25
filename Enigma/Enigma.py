class Rotor():
    def __init__(self):
        self.Start = "A"
        self.Letter = self.Start
        self.Name = "!"

    def State(self):
        print(self.Letter)

    def Rename(self, Name):
        self.Name = str(Name)
    
    def Settings(self):
        print("This is ", self.Name)
        print("Start Position: ", self.Start)

    def Position(self, Position):
        self.Start = str(Position)

print("* Enigma * \n")

One = Rotor()
Two = Rotor()
Three = Rotor()

# Names
One.Rename("Rotor 1")
Two.Rename("Rotor 2")
Three.Rename("Rotor 3")

# Output

One.Settings()
print("")

Two.Settings()
print("")

Three.Settings()