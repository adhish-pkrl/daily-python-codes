######Data Types

#identify data type
x = 6.0
print(type(x))

#Each variable for Built-in data type

x = 4
p = 3.14
a = 1 + 3j
nm = "Adhish"

w = 6
e = 12
print(w< e) #boolean -->True

r = None
print(r)

#list
books = ["math", "English", "Social"]
print(books)    

#tuple
intgrs = (5, 6, 8, 23, 45, 67)
print(intgrs)

#set
rollno = {1, 2, 3, 4, 5, 6, 7}
print(rollno)

#using the ' type()' function 
print(type(rollno))   #set


#list into touple
books = tuple(books)
print(books)  #tuple
print(type(books))

#tuple into list
intgrs = list(intgrs)
print(intgrs)  #list 
print(type(intgrs))


#Dictionary containing Student information
students = {
    "name" : "Adhish",
    "stid" : 104,
    "jionYear" : 2025,
    "faculty" : "Humanities"
}
print(students)


#Data Types of Mutable and Immutable

"""
Mutable data types can be modified after Creation 
Immutable data types cannot be modified after Creation 

"""

#Mutable
j = [44, 53, 55, 22]
print("Before change: ", j)

#changing
j.append(65) #modified
print("After change: ", j)

#immutable
name = "Adhish"
print("before change: ", name)

#changing
####name[0] = "S"
#####print("After change: ", name) # it shows error Cuz it's Immutable

#We should change likke this
name = "S" + name[1:]
print("new String: ", name)


#Store different data types inside a list.--->Mathii garii sake


#Comparing list, tuple, and set.

#list
"""
ordered, allows duplicates, mutalbe

"""

#Tuple
"""
ordered, allows duplication, immutable

"""

#set 
"""
unordered, no Duplicates, mutable

"""

###########demonstrating different data types.#########
"""
int 
float
string
complex
bool
none

list
tuple
set
frozenset

@#$##Mathii nei Use vayee sabeii


"""

