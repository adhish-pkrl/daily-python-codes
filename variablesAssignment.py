#Variables
#variables to store name, age, & address

name = "Adhish"
age = 19
add = "Butwal"
print(name, age, add)

#swaping variables value
name, age = age, name

print("name:", name)
print("age: ", age)

#assign multiple values
x,y,z, = 19,67,93
print(x, y, z)

#assign same value 
a=b=c = 5
print(a)
print(b)
print(c)


#checking data type
print(type(a))
print(type(name))  # this is int cuz we swaped the value
print(type(age))   # this is str cuz we swaped the value


#program that calculates the sum
q = 3
r = 5
print(q+r)


#conversion  

#int to float:
x = float(1)

#float to int:
y = int(2.8)

#int to complex:
z = complex(1)
print(x, y, z)


#diffrence btwn Local and global variable

"""
local variable : function vitraa create garera, function vitra matreii use garna milxa

Global variable : Function bahira create garera Function vitra bahira 2tei ma Use garna milxa


"""

#variable name for Student information
nam = "Adhish"
std_ID = 103
addr = "Butwal"
faculty = "BCA"
section = "A"
print(f"The student name is {nam} , form {addr}, ID {std_ID}, faculty of {faculty}, Section {section} ")


#predict the output
d = 10
s = 5
d = s + 20
print(d)   