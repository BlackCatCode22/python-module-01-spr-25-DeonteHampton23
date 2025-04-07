class partyAnimal:
    def __init__(self) :
        self.x = 0
        print('I am constructed')
    def party(self) :
        self.x = self.x + 1
        print('So far', self.x)
    def __del__(self):
        print('I am destructed', self.x)

an = partyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

class partyAnimal :
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name,"constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name,"party count",self.x)
s = partyAnimal("Sally")
s.party()
j = partyAnimal("Jim")
j.party()
s.party()