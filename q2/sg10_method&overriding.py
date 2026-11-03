class Animal: #This creates a parent class, Animal
    def __init__(self, name): #This creates an attribute for the parent function
        self.name = name #This represents the name of the object
    def eat(self): #This method represents the object eating
        print(f'{self.name} eats') #This prints the output of the object eating
    
class Lion(Animal): #This creates a child class, Lion, inheriting the name attribute name of the parent
    def eat(self): #This method represents the object eating and overrides the inherited method from the parent
        print(f"{self.name} eats fresh meat.") #This prints the output of the object eating
    def make_sound(self): #This method represents the object making a sound relative to its species (Lion)
        print(f"{self.name} roars loudly!") #This prints the representation of the object lion roaring

class Elephant(Animal): #This creates a child class, Elephant, inheriting the name attribute name of the parent
    def eat(self): #This method represents the object eating and overrides the inherited method from the parent
        print(f"{self.name} eats grass and fruits.") #This prints the output of the object eating
    def make_sound(self): #This method represents the object making a sound relative to its species (Elephant)
        print(f"{self.name} trumphets!") #This prints the representation of the object elephant making a sound

class Monkey(Animal): #This creates a child class, Monkey, inheriting the attribute name of the parent
    def eat(self): #This method represents the object eating and overrides the inherited method from the parent
        print(f"{self.name} eats bananas.") #This prints the output of the object eating
    def make_sound(self): #This method represents the object making a sound relative to its species (Monkey)
        print(f"{self.name} chatters!") #This prints the representation of the object monkey making a sound

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound()
lion.eat()
print("-----")

elephant.make_sound()
elephant.eat()
print("-----")

monkey.make_sound()
monkey.eat()
print("-----")
