####Python Operatos

#Arithmetic Operators
a = 20
b = 6
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

#Assignment Operators
x  = 4
x +=3
x -= 1
x *=4
x /=2
x %=3
x **= 4


#Comparison Operator
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


#Logical Operators
print("Logical Operators")
p = 20
print(p > 4 and p < 80) #Both Conditions must be True--True
print(p> 5 or p < 15) #one condition true --True
print(not(p > 35 and p < 80))  #it's false but 'not' converts it into True


###Check whether a person is eligible to vote using and.
age = int(input("Enter your Age: "))
if age >= 18:
 print("You can vote")
else:
 print("Hat bachhaa")


#MemberShip Operator

fruits = { "apple", "orange", "Pineaple", "Cherry"}
print("orange" in fruits)
print("pomerranate" in fruits)

print("apple" not in fruits)
print("mango" not in fruits)




#Check whether a value exists in a list.
uu = [34, 543, 2, 66, 23, 66,75,98]

if 34 in uu:
 print("woHo xa xa")
else:
 print("Hyy vagban Xoina")

