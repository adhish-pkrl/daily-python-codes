###Again FUnction
"""
returns data
##Block of code
used to avoid writing code repeatedly

"""
#def --> define function
# def function_name( ):

def add(a,b):
    print(a+b)
add(4,5)

add(5,1)

"""
latter and underscore use finction created

"""
#return values
"""
data back to the code that called them using the return
"""
def get_greeting():
    return"Hello"
print(get_greeting())


#argument
#is the actual value that sent to the function when it is called

#paramater
#is the variable listed inside the parantheses in function definition


#practice qns
#greeting
def greeting(name):
    return("HELLO: ",  name)
print(greeting("Ram"))

#square
def square(num):
    return(num * num)
print(square(2))
print(square(4))

#odd even
def odd_even(nm):
    if nm % 2 ==0:
        return("even")
    else:
        return("odd")
print(odd_even(5))
print(odd_even(6))


#pos neg zero
def pos_neg(num):
    if num > 0:
        return("Positive")
    else:
        return("Negative")
print(pos_neg(-4))
print(pos_neg(3))


#lagest num between 2numbers
def largest_num(a,b):
    if a > b:
        return(a)
    else:
        return(b)
print(largest_num())

#electricity ko bill unit aanusar --unit pass garnii -- aanii jati poisa xa
# 0 - 100 unit = 5per unit
#101-200 unit = 7per unit
#201> unit = 10per unit

#5 diye 1+2+3+4+5 add garniii

