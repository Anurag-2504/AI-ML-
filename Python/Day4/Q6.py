'''
    Q6. Create an Abstract class Employee with an abstract method calculate_salary().
    create subsclass intern, Fulltimeemployee, and contract employee that implement the method differently.

'''
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Inter(Employee):

    def __init__(self,salary):
        self.salary=salary

    def calculate_salary(self):
        return self.salary

class FullTimeEmployee(Employee):

    def __init__(self,salary):
        self.salary=salary
    
    def calculate_salary(self):
        return self.salary
    
class ContractEmployee(Employee):
    def __init__(self,salary):
        self.salary=salary
    
    def calculate_salary(self):
        return self.salary
    
i1=Inter(10000)
print(f"Intern Stipend is : {i1.calculate_salary()}")

f1=FullTimeEmployee(95000)
print(f"Salary of employee : {f1.calculate_salary()}")

c1=ContractEmployee(35000)
print(f"Salary of Contract Employee : {c1.calculate_salary()}")
