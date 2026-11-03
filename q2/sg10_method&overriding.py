class Animal: #This creates a parent class, Animal
    def __init__(self, name): #This creates an attribute for the parent function
        self.name = name #This represents the name of the object
    def eat(self): #This method represents the object eating
        print(f'{self.name} eats')
    
class Lion(Animal): #This creates a child class, Lion, inheriting the name attribute name of the parent
    def eat(self): #This method represents the object eating
        print(f"{self.name} eats fresh meat.")
    def make_sound(self): #This method represents the object making a sound
        print(f"{self.name} roars loudly!")

class Elephant(Animal): #This creates a child class, Elephant, inheriting the name attribute name of the parent
    def eat(self): #This method represents the object eating
        print(f"{self.name} eats grass and fruits.")
    def make_sound(self): #This method represents the object making a sound
        print(f"{self.name} trumphets!")

class Monkey(Animal): #This creates a child class, Monkey, inheriting the attribute name of the parent
    def eat(self): #This method represents the object eating
        print(f"{self.name} eats bananas.")
    def make_sound(self): #This method represents the object making a sound
        print(f"{self.name} chatters!")

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
