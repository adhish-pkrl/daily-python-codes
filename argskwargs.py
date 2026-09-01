### *args
"""
if we do not know how many arguments will be
 passed into your function, add a * before the
 parameter name.
"""

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Email", "Tobias", "Linus")


#What is *args
# parameter allows a function to accept any number of positional argument
def my_args (*names):
    print("type", type(names))
    print("First name: ", names[0])
    print("second name: ", names[1])
    print("Third name: ", names[2])
    print(names)
my_args("Adhish", "King", "Pokharel","hero", "DOn", "Pura Khatraaaa")



#args with regular arguments
#we can combine regular parameters with *args.
#Regular paramater come before *args:

def greet(greeting, *person):
    for name in person:
        print(greeting, name)
greet("Namaskar", "Adhish", "Pratik", "sagar")



##Add nums with args function
def add_function(*num):
    total = 0
    for numbers in num:
        total += numbers
    return total

print(add_function(1,2,3))
print(add_function(10, 20, 30,40,10))
print(add_function(6))




### *kwargs
"""
if you do not know how many keyword arguments
 will be passed into your function, add two **
 before parameter name

"""
def my_fnt(**kid):
    print("His last name is "+kid["lname"])

my_fnt(fname= "tabies", lname = "refsnes")



def my_perFu(**myvar):
    print("Name: ", myvar["name"])
    print("class: ", myvar["clas"])
    print("ROll no: ", myvar["rollno"])

my_perFu(name = "Adhish", clas = "Bca", rollno = 5)

