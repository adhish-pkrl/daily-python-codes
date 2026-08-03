#CASTING

#convert int to float
x = 4
print(float(x))

#convert float into int
y = 3.94
print(int(y))

#string into Int
s = "143432"
print(int(s))
print(type(s))

#Int into String
t_in = 433
nm_st = str(t_in)
print(t_in)  #integer
print(type(nm_st)) #convert to String

#list to tuple
apple = ["red", "sweet", "Cold"]
apple = tuple(apple)
print(type(apple))  #Tuple

#tuple into list
banana = ("yelloe", "white", "sweet")
banana = list(banana)
print(type(banana))  # List

#list into set
apple = set(apple)
print(type(apple)) #set

#Set to list
marks = {24, 43, 55, 53, 23, 89}
print(type(marks)) #Set

marks = list(marks)
print(type(marks)) #List
 

#Implicit 
"""
Python automatically promotes smaller data types to longer ones when Needed

"""
num_int = 10
num_float = 20.34
print(num_int + num_float) #manage to convert ans into Float


#Explicit 
"""
YOu manually Convert one type into another using functions
"""
nm = 5.43
converted = int(nm) # Explicit casting

print(converted)

#predict the output after type casting

num_ans = num_int + num_float #int --> float ma aauxa ans
print(num_ans)

