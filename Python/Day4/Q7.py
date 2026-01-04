'''
Q7 
    . Create a class Person that allows the constructor to work with:
    • name only
    • name + age
    • name + age + address
    As direct constructor overloading (multiple constructors) are not allowed butwe have to use default
    parameters to simulate constructor overloading.

'''

class Person:

    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

    
p1=Person("Anurag Ratna")
p2=Person("Anurag Ratna",24)
p3=Person("Anurag Ratna",24,"Lucknow")

p1.display()
p2.display()
p3.display()
        