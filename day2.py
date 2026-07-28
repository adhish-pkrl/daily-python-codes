#Mulvariable
#x,y,z = 2,3,5
#print(x,y,x)

#global variable //Sabei leyy Access garna milnii (PUBLIC, Default vaye jastei Java maa)
# variables that are created outside of Functionn

#def random():
#    print(x)

#random()

y = "wow"

def pull():

    print(y)

pull()  #yo lai Function ko Bahira Lekhna parxa, if not tyo Run huna

a = 4
b = 3
print(a+b)

def roo():
    global x ##global vanera yesma KeyWord use garepar x laii Globally use garna sakixa
    x= 90  
    print(x) # yo local variable bataw value ligxa so value print hunxa
roo()
print(x)  #if global ma variable define xoina vanii tyo ma error aauxa 
    # maile Mathii "global" use gareko xu so aabaw X ko value neii Print hunxa



    ####DATA TYPES #####
#build in data types 
"""
text type : str
numeric : int , float, complex (z = 1i #i lai mix garnu)
sequence : list, tuple,dictonary, range 
mapping : dict 
set types: set, forzenset
boolen type : bool
binary : bytes
nontype: nontype

"""

#list
football_palyears= ["ronaldo, messi, Halend, Mbappe"]
print(football_palyears)


#random function
import random
print(random.randrange(1,100))  # every time random number print garxa

# self check for random functions methods

#voli String
