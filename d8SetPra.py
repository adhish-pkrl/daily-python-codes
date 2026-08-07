##SEt
#Access Set
thisset = {"apple", "banana","mango"}
for x in thisset:
    print(x)

#check item is in the set or not
print("mango" in thisset)
print("banana" in thisset)
print("cherry" in thisset)

#Add set item
thisset.add("papaya")
print(thisset)


tropical = {"pineapple", "dragonFruit"}

thisset.update(tropical)
print(thisset)


#remove set item
thisset.remove("banana")
print(thisset)

thisset.discard("papaya")
print(thisset)


y = thisset.pop()
print(y)

# del thisset
# print(thisset)

# thisset.clear()
# print(thisset)


##Join set
names ={"Adhish", "Pratik", "Prasun", "Sujal"}
print(names)

studenta = {"Amrit", "Sujan", "Aayush"}
#stndts = names | studenta
#print(stndts)

#stdnts = names.union(studenta)
#print(stdnts)

studenta.update(names)
print(studenta)
print(names)


###Intersection
"""
the intersection() method will return a new set,
that only contains the items that are present in both sets

"""
people = {"Dipesh", "Sagar", "Arjun","Baburam"}
friends = {"Arjun", "Dipesh","Nerandra", "Bishnu"}


#common value print garxa
bst = people.intersection(friends)
print("Brothers:",bst)

#different value print garxa
nono = people.difference(friends)
print(nono)

#SAME DIFFRENCE nei aauxa
heii = people - friends
print(heii)

#diffrence value lai euta set ma add garera Update garxa
friends.difference_update(people)
print(friends)

#aabaw difference value lai matrei print garxa --Mathi ko jastei neii same ho
#EX:
friends.symmetric_difference(people)
print(friends)


