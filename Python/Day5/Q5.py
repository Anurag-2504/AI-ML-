'''
    Q5 
    . Write a program that tries to open ta.txt"in read mode. If the file does not
    exist, catch the exception and print "File not found!".
'''
try:

    with open("Python/Day5/Data.txt","r") as f:
        print(f.read())
    
except FileNotFoundError:
    print("File not found!")
finally:
    print("This statement going to execute finally!")