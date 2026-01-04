'''Q3. Write a function that prints the digits of a number, n .'''

# In Correct order 
def digits(num):
    for i in str(abs(num)):
        print(i)


# Reverse Order
'''def digits(num):
    while num != 0:
        print(num % 10)
        num = num // 10
'''
digits(9876)
