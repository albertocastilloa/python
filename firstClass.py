class Animal(object):
    is_alive = True
    health = "Good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        print(self.name)
        print(self.age)


hippo = Animal("Bumpty", 13)
sloth = Animal("Pato", 15)
ocelot =Animal("Crunch", 3)

print(hippo.health)
print(sloth.health)
print(ocelot.health)