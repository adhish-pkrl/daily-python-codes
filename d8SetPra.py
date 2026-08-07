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