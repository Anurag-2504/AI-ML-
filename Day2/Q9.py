'''Q9. Write a function i s _ p r i m e ( n ) t h a t returns T r u e if n is a prime number and
False otherwise, using a loop.'''

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(7))
print(is_prime(36))
print(is_prime(43))

'''
    output:
    True
    False
    True
'''