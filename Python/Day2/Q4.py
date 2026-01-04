'''Q4. Write a function to return the count the number of digits in a number, n.'''

def count_num(num):
    counter=0
    for i in str(abs(num)):
        counter+=1
    print(counter)

count_num(101022)