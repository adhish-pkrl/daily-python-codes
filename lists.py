#LISTS

#Create a list of five fruits.
fruits = ["banana", "apple", "orange","cherry", "mango"]
print(fruits)


#Create a list of student names.
std_name = ["Adhish", "Pratik", "Sujal", "Rahul","Prasun"]
print(std_name)

#Create a list containing different data types.
dtty = ['adhish', 54, 67.75, "Wohoo"]
print(dtty)


#Create an empty list.
empty = [""]
print(empty)

#Create a nested list.
nst_list = [
    ["Hari", 18, "can Vote"],
    ["Ram", 43, "can vote"],
    ["Shyam", 14, "Cannot vote"]
]
print(nst_list)

print(nst_list[0][0]) #Hari
print(nst_list[1][1]) #43
print(nst_list[2][2]) #cannot vote


#Create a list using the list() constructor.
"""

so 'list()'  constructor converts any Iterable(String, tuple, range, set) into --> List

"""
print("After this List()")

# Create a list using list() constructor

# From a string → splits into characters
list1 = list("Adhish")
print("list1:", list1)

# From another iterable (tuple)
list2 = list((1, 2, 3, 4))
print("list2:", list2)

# From a set
list4 = list({10, 20, 30})
print("list4:", list4)

# lst1 = list("Adhish")
# print(lst1)

# lst2 = list(1, 4, 5, 7)
# print(lst2)

# # lst3 = list({34, 53, 5645, 54})
# # print(lst3)


#Create a list of numbers from 1 to 10.
numLst = [1,2,3,4,5,6,7,8,9,10]
print(numLst)

#Create a list of even numbers.
evn_lst = [ 2, 4, 6, 8, 10]
print(evn_lst)

#Create a list of odd numbers.
odd_lst = [1, 3, 5, 7, 9]
print(odd_lst)


#Store marks of five students in a list.
marks = [98, 53, 54, 23, 55, 74,45]
print("All Students marks: ", marks)

#for each Student
print("Student1", marks[0])
print("Student2", marks[1])
print("Student3", marks[2])
print("Student4", marks[3])
print("Student5", marks[4])
print("Student6", marks[5])



####Accesing List Items###:::
#Print the first element.
name = ["roshan", "ram", "Shyam", "Gita", "Rita","bishnu", "Mukunda", "Pashupati"]
print("fitst element :", name[0])

#Print the last element
print("Last element: ", name[4])


#Print the third element.
print("third element: ", name[2])

#element using neg index
print("4th name:", name[-2]) #Gita


#Print elements from index 2 to 5.
print(name[2:5])


#Print every second element.
print("Every Second Element:", marks[::2]) ##' :: ' --> ley kati kati ko gap ma Ko element print garnii vanxa


#Reverse the list using slicing.
newmarks = marks[::-1]
print("Original list: ", marks)
print("reversed list: ", newmarks)

#find length of String
print(len(marks))

#Check whether an item exists.
print(54 in marks) # True
print("Ram" in name) #false

#Using if Condition 
if 98 in marks:
    print("Yes it Exits")
else:
    print("It's does not exist")


#Iterate thorugh all the List item
for mark in marks:
    print(mark)



####Changing List Item####
print("After this changing List")
#Replace the first item
marks[0] = 95
print(marks)

name[1] = "Purnima"
print(name)


#Replace the last item.
name[7] = "Mahesh"
print(name)

#Changing multiple list items.
marks[0:3] = [34,12,31,50]
print(marks)


name[0] = "adhish"
name[3] = "Pratik"
name[6] = "Prasun"
print("After Replace the NAmes: ", name)

#Replace items using slicing.
print("After this Slicing")
students = ["bimal", "himal", "Bhuwan", "Bikash", "gopal"]

print("before slicing: ", students)

students[0:2] = ["Ankit", "shishir"] ##Bimal ko rah Himal lai replace
print("After slicing:", students)

students[-2:] = ["Binita", "Sarswata"]
print("Poxi ko name change :", students)


#names to uppercase.
pagals = ["milan", "BISHAL", "Saroj", "PRADIP","Dipes", "RANJIT"]
print("Original list:", pagals)

#convert all names to uppercase
pagals = [nam.upper() for nam in pagals]
print("Updated list (uppercase): ",pagals)

#lower case
pagals = [num.lower() for num in pagals]
print("Lower case:", pagals)



#Update the Student Marks
##marks = [98, 53, 54, 23, 55, 74,45]

marks[0] = 43
marks[4] = 12
print(marks,"After update")


#Replace all the Even List with '0'
evn_lst = [0 if num %2 ==0 else num for num in evn_lst]
print("Updated list: ", evn_lst)

#Replace all odd numbers into 1
odd_lst = [1 if dum % 2 != 0 else dum for dum in odd_lst]
print("Updated odd list : ", odd_lst)


