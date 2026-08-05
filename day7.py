#Tuples
#multiple elements and Items ---->store data type
"""
tuples are written inside small bracket 
i.e = '()'
#Features
duplacete allow 
ordered
immutalbe / Unchangeble ==After they are created

"""
variable = ("Adhish", "Pratik", "Sujal", "Prasun", "Adhish","Sujal","Prasun")
print(variable)
print(type(variable))
print(len(variable))

##variable[0] = "Aadhu" #Shows error cuz it's immutable
##print(variable)

newvariable = list(variable)
print(type(newvariable))

newvariable [2] = "Pinkey"
print(newvariable)





###unpack 
"""
.count -->Specific value katii Chotii aako xa vanera Print huxna

"""
print(variable.count("Adhish"))