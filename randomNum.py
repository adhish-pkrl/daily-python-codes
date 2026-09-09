##Random Number in NumPy
"""
Random number does not mean a different,,
    number every time.
    *Random means something that can not be predicted logically
"""

##generate a random number
from numpy import random

x = random.randint(100)
print(x)


##generate random Float
from numpy import random

y = random.rand()
print("random float: ",y)



##generate an random array
from numpy import random

z = random.randint(100, size=(5))
print("Random array:", z)

#generate 2-D array
a = random.randint(10, size = (4,3))
print("Random 2-D array:", a)


#random array with float numbers
b = random.rand(3,2)
print("Float value array: ",b)



##Generate random number from Array
"""
choice() method allows you to generate a random value based on an array of values

"""
from numpy import random
c = random.choice([3,5,7,9])
print(x)