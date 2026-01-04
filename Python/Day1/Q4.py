'''
Q4. The user enters a string containing a number (e.g.," 4 5 " ). Convert it to:
    • an integer
    • a float
    • a string again
    Print all three values with their types.

'''
user_input = input("Enter  a number: ")
print("New Type:", type(int(user_input)))
print("New Type:", type(float(user_input)))
print("New Type:", type(str(user_input)))