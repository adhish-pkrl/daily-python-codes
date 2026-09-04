##Iterators
"""
an iterator is an object that contains a countable number of values
lists, tuple, dictionaries, and sets are all iterable objects

"""
mylst = ["ram", "shyam", "Hari","Adhish", "Pratik"]
myit = iter(mylst)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#Characters iterable
mystr = "Adhish"
myitstr = iter(mystr)

print(next(myitstr))    #A
print(next(myitstr))    #d
print(next(myitstr))    #h
print(next(myitstr))    #i
print(next(myitstr))    #s
print(next(myitstr))    #h




#Looping through an iterator
mytuple = ("hello", "My", "Name", "Is", "Adhish")
for x in mytuple:
    print("Looping iterator printing: \n",x)
