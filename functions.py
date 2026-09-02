#decorator
"""
decorator let you add extra behaviour to a function

"""

def my_function(kig):
    def myinner():
        return kig().upper()
    return myinner

@my_function
def change():
    return "Adhish Pokharel"

print(change())



###Lambda
"""
A lambda function is a small  anonymous function
A lambda function can take any number of arguments,
    but can only have one expression

temporary function...created when we want to use it once..

"""

x = lambda a ,b : a *b
print(x(5,6))

y = lambda c, i: c % i
print(y(20, 3))


#lambda with map()
numbers = [1,2,3,4,5,6,4,5,6]
mul = list(map(lambda x: x * 4,
numbers))
print(mul)