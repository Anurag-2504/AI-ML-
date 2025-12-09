'''
Q5 
    Create a base class Vehicle with attribute like brand and model.
    Create two sub class car and bike the extra attributes - seats(car) and engine_cc(bike)

'''

class Vehicle:
    
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Car(Vehicle):

    def __init__(self, brand, model,seats):
        super().__init__(brand, model)
        self.seats=seats

    def display(self):
        print(f" Brand is {self.brand}, and model is {self.model}, and number of seats {self.seats}")

class Bike(Vehicle):
        def __init__(self, brand, model,engine_cc):
             super().__init__(brand, model)
             self.engine_cc=engine_cc

        def display(self):
             print(f" Brand is {self.brand}, and model is {self.model}, and engine in cc {self.engine_cc}")

c1=Car("Sokda","saliva",5)
c1.display()

b1=Bike("Royal Enfield","Hunter",350)
b1.display()