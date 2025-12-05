''''Q7. Design a program to continuously input a number n from user & print if it is
positive or negative until the user enters "Quit".'''


while True:
    print("Enter 0 for Quit")
    num=int(input("Enter a number : "))
    if num<0:
        print("Negative")
    elif num==0:
        break
    else:
        print("Positive")
