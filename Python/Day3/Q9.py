'''Q9. Given a list, print all elements that appear more than once in the list.'''

list_name=["Anurag","Abhishek","Amit","Ritik","Adarsh","Anurag","Ritik","Abhishek"]

duplicates = set([x for x in list_name if list_name.count(x) > 1])
print("Elements appearing more than once:", duplicates)