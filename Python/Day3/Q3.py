'''Q3. Input two lists of integers from the user. Merge them into one list and sort the
r e s u l t .'''

l1 = list(map(int, input("List 1: ").split()))
l2 = list(map(int, input("List 2: ").split()))

print(sorted(l1 + l2))
