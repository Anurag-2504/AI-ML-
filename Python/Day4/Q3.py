''' Q3.
        Create a class Student private with attributes _name, _roll_no, and _marks.
        Provide getter setter and methods with validation (e.g., marks cannot be
        negative, roll number has to be between 1 & 100 & name cannot be empty).
'''

class Student:
    
    def __init__(self,name,roll_no,marks):
        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks

    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    def get_marks(self):
        return self.__marks
    
    def set_name(self, name):
        if name.strip() == "":
            print("Name cannot be empty.")
        else:
            self.__name = name

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100.")

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative.")


s = Student("", 150, 100)  


s.set_name("Anurag Ratna")
s.set_roll_no(21)
s.set_marks(98)

print(s.get_name())
print(s.get_roll_no())
print(s.get_marks())
    