'''Q8. Write a program to check whether two lists share no common elements.'''

list1=[1,2,3,4,5]
list2=[6,7]

if set(list1).intersection(set(list2)):
    print("Common elements are present.")
else:
    print("No common element.")