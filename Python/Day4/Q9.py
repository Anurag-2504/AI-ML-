'''
Q9 
    . Create the following classes: Herbivore, Carnivore, Omnivore with some
    attributes & methods. Then create a class Bear that inherits from all the above
    classes to showcase how multiple inheritance works.
'''
class Herbivore:
    def eat_plants(self):
        print("Eats plants")

class Carnivore:
    def eat_meat(self):
        print("Eats meat")

class Omnivore:
    def eat_both(self):
        print("Eats both plants and meat")

class Bear(Herbivore, Carnivore, Omnivore):
    def sound(self):
        print("Bear growls")

b1=Bear()
b1.eat_plants()
b1.eat_meat()
b1.eat_both()
b1.sound()
