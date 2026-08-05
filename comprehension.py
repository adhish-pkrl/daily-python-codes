###List--Comprehension #####
"""
list compresension is a compact way to create lists in Python
Insted of writing a loop and appending items, you can build the list in one line.
"""
#Syntax
"""
[expressoion for item in iterable if condition]

expression --> What you want to Store in the list
item --> Variable representing each element 
iterable --> sequence(list, range, string, etc.)
condition(optional) --> filter elements
"""
#Example::
numbers = [1,2,3,4,5,6]
squares = [num**2 for num in numbers]
print(squares)



#With Condition
even_squares = [num**2 for num in numbers if num % 2 == 0]
print(even_squares)

#odd numbers
odd_squares = [num**2 for num in numbers if num % 2 != 0]
print(odd_squares)


#convert all names to uppercase
names = ["biplap", "manish", "sambhu", "ram"," ", "hari","binita"," ","sabina"]
upper_name = [name.upper() for name in names]
print(upper_name)



#Filter numbers greater than 50.
number = [34,53,64,23,2,4,6,77,4,534,64,98]
flt_num = [num for num in number if num >= 50]
print(flt_num)


#Create a list of String lengths
print(names)
lengths = [len(name) for name in names]
print("String Lengths: ", lengths)


#Remove empty String
filtered_names = [name for name in names if name !=" "]
print(filtered_names)

#print only empty string
blank_names = [name for name in names if name == " "]
print(blank_names)


#Generate a multiplication table
n = 2
table_of_2 =[n * i for i in range(1,11)]
print(f"Multiplication table of {n}: ", table_of_2)

