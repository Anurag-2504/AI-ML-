'''Q5. Write a function to return the sum of digits of a number, n .'''

def sum_of_digits(num):
    sum=0
    while num!=0:
        sum = sum + num%10
        num= num//10
    print(sum)

sum_of_digits(123456)