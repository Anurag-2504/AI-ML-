'''
   Q2. Take two numbers as input from the user and print their sum, difference,
       product, and quotient.
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product", num1 * num2)
if num2 != 0:
    print("Quotient:", num1 / num2)
else:
    print("Quotient:  Undefined (cannot divide by zero)")