''' Given a list of words:
    words = [ " apple " " banana " , " kiwi " " cherry " "mango"]
    Create a dictionary that maps each word to its length.
'''

words = [ "apple","banana","kiwi","cherry","mango"]
len_mapper={}

for i in words:
    word=i
    length=len(i)
    len_mapper[word]=length

print(len_mapper)
