##Operatorss 
#Arithmetic vaiiSakyo


"""

"""

#Assignment Operators

x = 5  #" = " ley x ma 5 ko value dinxa
print(x)

x += 4
print(x)

x -= 2
print(x)

x *= 3
print(x)

x/=2
print(x)

x %= 3
print(x)

x // 3
print(x)

x **= 2
print(x)

#x &= 3
#print(x)

#x |= 3 
#print(x)

#x ^= 3
#print(x)

#x >>= 3
# print(x)

# x <<= 3
# print(x) 


print(x:=3)





## Ternary Operator
"""
The ternary operator allows you to assign one value if a condition is true, and another if it is false::

"""
num = 6 
x = "weekend!!" if num > 5 else "workday"
print(x)

#age = int(input("Enter your age: "))
#age = "You can Vote" if age >18 else "Pak hattt"
#print(age)

z = "fri" if num == 5 else "sat" if num == 4 else "sunn" if num ==7 else num == 6 if "Xutiii hoo gaiii " else "Weekday"
print(z)



#Comparision Operators 
s = 2
a = 100

#equal
print(a==s)  #if right "True" if  not "false"

#not Equal
print(a != s) # equal naVaye True hunxa 

#greater than
print(a > s)

#less than
print(a<s)

#greater than or Equal to 
print(a>= s)

#less than or Eual to
print(a <= s)

# x = 5
# y = 3

# print(x <= y)



#logical Operators
#Logical operators are used to combine conditional Statement 
chi = 35
chpt = 50
print(chi + chpt)

#and  --> returns if both statements are true
print(chi < 90 and chpt > 30) #2tei Condition True vayee

#or --> returns if one of the Statement is True 
print (chi < 10 or chpt > 20) # euta vayenii true xa

print (chi < 10 or chpt < 20) #2tei wrong 


# not --> reverse the Ans, like if ans is right converts into false, if false cinverts into True

print(not(chi < 3 and  chpt <10)) # false ho but True print vayo

print("yo vanda tala Identity Operators")
#Identity operators
"""
used to compare the objects, not if they are equal, but if the are actually the same object, with the same memory location 

"""

#is --> Returns true if both Variables are the same Objects
d = ["apple", "banana"]
k = ["apple", "banana"]

m = d
print(d is m)
#true cuz m is the same obj as d

print(d is k)  #false cuz d and k same object hoinan --value same vaye Panii false hunxa

print(d == k)
#True hunxa Cuz "==" leyy value same vako kura Denote garxa

print (d is not k)
#true hunxa CUz d obj ra K obj same hoina value same vayePaniii



print("yeha vanda tala Membership operators")
##MemberShip Operators
"""
used to test if a sequence is presented in an object 

"""

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("orange" in fruits)
print("pineaple" not in fruits)
print("apple" not in fruits)

name = "Adhish"
print("h" in name)
print("u" in name)

#not
print("i" not in name)
print("j" not in name)
 



