'''Q4. Given a tuple of integers, create:
• A tuple of all even numbers
• A tuple of all odd numbers'''

num_tup=(8,2,1,4,29,3,5,7,10,22)

even_tuple = tuple(num for num in num_tup if num % 2 == 0)
odd_tuple  = tuple(num for num in num_tup if num % 2 != 0)

print("Even number : ",even_tuple)
print("Odd number : ",odd_tuple)