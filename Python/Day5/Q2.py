'''
    Q2
    . Create a program that:
    1. Opens a file "log.txt"
    in append mode
    2.Adds a new log entry (like "Program run successf
    ully")
    3.Opens the file in read mode and prints all logs
'''
with open("Python/Day5/logs.txt","a") as f:
    f.write("Program run successfully")

with open("Python/Day5/logs.txt","r") as f:
    print(f.read())