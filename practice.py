#String concatenation 
a  = "hello Adhish"
b = "k xa "
c= a + b 
print(c)


d = a + " " + b    #adding space between them
print(d)

#f string
age = 19
inf = f"My name is Adhish, I'm {age} years old. "
print(inf)
print(f"My name is Adhish, I'm {age} years old")   ##Both are valid 



#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 


##String Methos 
f = "adHISh."
print(f.capitalize()) #Converts the first character to upper CASE
print(f.casefold())  # COnversing String into Lower case
print(f.center(50))  # tyo Name laii Print huni Display ma Center ma Print garxa\
print(f.count(f))    #Returns the number of times a specified value occurs in a string
# print(f.encode())    
#x = f.endswith(.)
print(f.endswith("h"))  #last ko character j xa tyo vaye True if not then false

x = "A \ D\ H\ I\ S\ H "
x = f.expandtabs(3)
print(f.expandtabs(2))


q= "Pagalll hoo  MAnxeyy "
z = q.replace("MAnxeyy", "Badarr")
print(z)

print(f.swapcase())   #Swap hunxa Upper case lai Lower aanii Lower case laiii Upper Ma
