##Booleans Py##

#Create variables with True and False.
age = 45
print(age > 10) ##True

print(age< 4) ##False


x = 4
y = 10


#Comparision Operators
print(x == y)
print(x != y)
print(x > y)
print(x<y)
print(x>=y)
print(x <= y)


#check num is nev or not
if x < 0 :
 print(x, "is neg")
else:
 print(x, "is pos")

#just normal 
print(x < 0)  #false

print(x > 0) # true


#check num is even or odd
num = 12
if num % 2 == 0:
 print(num, "is even")
else:
 print(num, "is odd")

#Check if a student passed (marks ≥ 40).

mark = 60

if mark >= 40:
 print("student is passed the Exam")
else: 
 print("Tah fail vaiss vaii")


## Evaluate Boolean Expression 

a = 10
b = 20

print("a > b:", a > b) 
print("a < b:", a < b)       
print("a == b:", a == b)   
print("a != b:", a != b)    
print("(a < b) and (a == 10):", (a < b) and (a == 10))  # True
print("(a > b) or (b == 20):", (a > b) or (b == 20))    # True


#using bool()
print(bool()) #false
print(bool(4)) #true

print(bool("")) #false
print(bool('Adhish')) #true

print(bool([])) #False
print(bool([1, 3 , 4])) #True


#none
print(bool(None)) #false

#sets
print(bool(set())) #false
print(bool({10, 30, 50, 70})) #True


#program usig boolean
###mathi neii gareko 


#Explain truthy ans Falsv values
"""

Mathi gari sakeko code line :66 to 81

"""
