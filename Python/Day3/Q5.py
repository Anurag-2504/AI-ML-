'''Q5. Create a dictionary where:
    • Keys = s t u d e n t n a m e s
    • Va l u e s = m a r k s (integer)
    Write a menu-based program where user presses a key ('A, 'B', 'C', 'D')
    depending on the operation they want to perform on the dictionary:
    1. A - Add a student
    2 . B - Update marks
    3 . C - Search for a student
    4. D - Display all students and marks
    5. E - Exit
'''
students ={}

while True:
    print("\n----- MENU -----")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students")
    print("E - Exit")

    choice = input("Enter your choice (A/B/C/D/E): ").upper()

    if choice=="A":
        name=input("Enter name : ")
        marks=int(input("Enter marks : "))
        students[name]=marks
        print("Student added successfully...")

    elif choice=="B":
        name=input("Enter name : ")
        if name in students:
            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")
    elif choice=="C":
        name=input("Enter name : ")
        if name in students:
            print(f"{name} → {students[name]} marks")
        else:
            print("Student not found!")
    elif choice=="D":
        print("All Student : ")
        print(students)
    elif choice=='E':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter A, B, C, D, or E.")

