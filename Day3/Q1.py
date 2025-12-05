'''Q1. Ask the user for a string and check whether it is a palindrome or not.
A palindrome is a string which is same when we read it forward & backward. Eg -
"madam", "racecar" etc.'''

user_str=input("Enter a String : ")
if user_str==user_str[::-1]:
    print("String is Palindrom")
else:
    print("String is not Palindrom")