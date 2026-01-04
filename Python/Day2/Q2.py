'''Q2. Write a function that takes two integers a and b and prints all even
numbers between them (inclusive).'''

def even(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)
        else:
            continue

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the  second number : "))

even(num1,num2)