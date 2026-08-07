####FROZENset 
"""
forzenset is an immutable varsion of a set
like sets, it contains unique, unordered, unchangable elements.
Unlike sets, elements cannot be added or removed from a frozenset../

"""
#Ex:
x = frozenset({"apple", "banana"})
print(x)
print(type(x))

###Methods and Shortcuts

#copy
fs = frozenset({1,2,3})
cp = fs.copy()
print(fs)
print(cp)

#diffrence
a = frozenset({1,2,3,4})
b= frozenset({3,4,5,6})
print(a.difference(b))
print(a - b)

#intersection
#already done

#isdisjoint()
"""
Returns true if there is no intersection between two frozensets.
"""
a = frozenset({1,2,3,4})
b= frozenset({3,4,5,6})
c = frozenset({5,8,6,7})
print(a.isdisjoint(b))  ##False
print(a.isdisjoint(c))  ##True 


##issubset()
"""
It checks wheather all elements 
of one set are contained inside another set
"""
print("After this Issubset's Output")
a = frozenset({3,4})
b= frozenset({3,4,5,6})
c = frozenset({5,6,})
print(a.issubset(b)) #True cuz a ko element b ma xan

print(a.issubset(c)) #False cuz a ko elements c ma xoinan

print(c.issubset(b)) #True cuz c ko element b ma xan



#issuperset()
print("after this all outpus from issuperset()")
a = frozenset({1, 2})
b = frozenset({1, 2, 3})

print(b.issuperset(a)) ##True -- a ko sabei b ma xan
print(a.issuperset(b)) ##False --b ko sabeii a ma xoinan

