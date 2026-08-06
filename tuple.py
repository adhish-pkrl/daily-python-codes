####Tuple#####
"""
tuple are used to store multiple items in a Single variable

"""
#Qn.1 __Access Tuples
"""Create a tuple conatain the names of six countries..
    write a program to::
    1.print the first element
    2.print the last element
    3.print the fouth element
    4.print the elements from index 2 to index 4 using slicing

"""
countries = ("Nepal", "India", "Pakistan", "Bhutan","japan")
print("First element: ", countries[0])
print("last element: ", countries[-1])
print("fourth element: ", countries[3])
print("First element: ", countries[0:5])


#Qn. 2__Update Tuples
"""Create a tuple containing five programming languages. Write a program to:
    1.Add a new programming language to the tuple.
    2.Remove one existing programming language from the tuple.
    3.Print the updated tuple.

"""
pro_lang = ("Python", "Java", "CSS", "C++", "HTML")
print("Before adding new language::", pro_lang)

#convert tuple into list
new_lst = list((pro_lang))
print(new_lst)

#Adding a lang..
new_lst.append("Go")
print(new_lst)

#removing the lang..
new_lst.remove("Java")
print(new_lst)



#Qn.3__Unpack Tuples
"""Create a tuple containing the following information of a Student:
 1.Name
 2.Age
 3.Faculty
 4.Semester
 5.College

"""
student = ("Adhish", 19, "BCA","Butwal kalika Campus", "Butwal -10","Ramnagar" )
#print(f"My names is {student[0]}, I\'m {student[1]} years old, Studying faculty of {student[2]}, at {student[3]}.")

#Using Unpacking
name, age, faculty, *college = student
print(name)
print(age)
print(faculty)
print(college)


#Qn.4__Loop Tuples & Tuple Method
""" Create a tuple of ten interers(include some repeated values). Write a Program to
 1.Display all elements using a for loop
 2.Display all elements using a while loop
 3.Find the number of times a particular value appears in the tuple
 4.Find the index of given value

"""
#1-Ans = 
numbers = (32,44,6,44,6,43,33,32,77,44,3,6,34,96,33)
for x in numbers:
    print(x)

#2-Ans=
print("After this Ans from While loop:")
i = 0
while i < len(numbers):
    print(numbers[i])
    i +=1


#3-Ans=
count_num = numbers.count(33)
print("33 appears: ", count_num)


#4-Ans=
index_of_num = numbers.index(77)
print(index_of_num)



#Qn-5 Join Tuples
"""Create two tuples:
 1.The first tuple should contain the names of three fruits
 2.The second tuple should contain the names of three vegetables.

-Write a program to :
 i.Join both tuples into a single tuple.
 ii.Print the joined tuple.
 iii.Print the total number of elements in the joined tuple.
 iv.Check whether a given item exists in the joined tuple.

"""
#1-Ans=
fruits =("Apple", "Orange", "Papaya")
print(fruits)

#2-Ans=
vegetables = ("Broccoli", "Carrots", "Tomatos")
print(vegetables)

# i-Ans=
new_tup = fruits + vegetables
#ii-Ans=
print(new_tup)

#iii-Ans=
print(len(new_tup))

#iv-Ans=
item = "Tomato"
if item in new_tup:
    print(item,"yes it's exist")
else:
    print(item, "does not exis in the joined tuple")

