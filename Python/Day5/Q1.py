'''
    Q1
    . Create a program that:
    1. Opens a file "names.txt"
    in write mode
    2.Writes 5 names (one per line) entered by the user
    3.Then opens the same file in read mode and prints all names
'''
with open("Python/Day5/names.txt","w") as f:
    for i in range(5):
        data=input(f"Enter {i} name : ")
        f.write(data+"\n")
with open("Python/Day5/names.txt","r") as f:
    print(f.read())