'''Q7. Write a program that takes a string from the user and prints the number of
spaces in the string.'''

user_str=input("Enter a string : ")
count=0
for i in user_str:
    if i==" ":
        count+=1
    else:
        continue
print(f"Number of blank space is : {count}")