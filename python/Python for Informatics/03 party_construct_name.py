
class PartyAnimal:
    x = 0
    name = ""
    
    def __init__(self, z):
        self.name = z
        print self.name, "constructed"
    
    def party(self):
        self.x = self.x + 1
        print self.name, "party count", self.x
        
    def __del__(self):
        print self.name, "destructed"
        
        
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
j.party()



# I am constructed
# So far 1
# So far 2
# So far 3
# I am destructed 3

