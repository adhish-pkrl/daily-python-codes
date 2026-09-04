##Set \
"""
store multiple value '{}'

1.unordered

2.unchangable--can remove and add

3. but we can add and remove item

4.do not allow duplicate value

"""
this = set(("banana"))
print(type(this))

#Access Item
item = {"apple", "banana", "cherry","apple","Papaya","cherry","orange"}
for x in item:
    print(x)

for x in item:
    print("cherry" in x)



#change item
"""
once we created set it cannot be changed

"""

##item.append("Pomogranate")
##print(item)

item.add("sewuu")
print(item)

item.remove("banana")
item.discard("cherry")
print(item)

item.pop()
print(item)

item.clear()
print(item)



####Set loops
##aafei hernii


#join set
#aafei herni


#dictonary 
#dictonary is used to store data values in key:value pairs
"""
written in curly braces
do not allow duplicate value

"""
#EX
student = {
    #keys : value --form ma write garniii
    "name" : "Adhish",
    "age" : 19
}
print(student)

#get  the value 
print(student['name'])
print(student.get('name'))


##CHANGE value
student["age"] = "huhu"
print(student)

#Value hernii all
print(student.values())



#ADD items
student["colour"] = "Blue"
print(student)


##gET ITEMS
"""
tuple ma value print garxa
"""
print(student.itemsv())