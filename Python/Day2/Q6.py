'''Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3
and 5.'''

def dev_check():
    for num in range(1,100+1):
        if num%3==0 and num%5==0:
            print(num)

dev_check()