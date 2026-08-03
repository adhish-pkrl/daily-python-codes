#STRINGS

#Create a string containing your full name.

name = "Adhish Pokharel"

#Print the first and last character of a string.
print("first character: ", name[0])
print("Last Character: ", name[14])

#Convert a string to uppercase.
print(name.upper())

#lower case
print(name.lower())


#count teh length of String
print(len(name)) #15 

#Reversed the Number of String
reverse_name = name[::-1]
print(reverse_name)

#check Substring Exists

myintro = "I\'m Adhish Pokharel, and I\'m learning Python"
substring1 = "Python"
substring2 = "Adhish"
substring3 = "Hero"

#using in operator
print("Does SubString1 Exist: ", substring1 in myintro)
print("Does SubString2 Exist: ", substring2 in myintro)
print("Does SubString3 Exist: ", substring3 in myintro)

#using find -->If exist it shows the Index value if not Shows -1
print("Index of Substring1 :", myintro.find(substring1))
print("Index of Substring2 :", myintro.find(substring2))
print("Index of Substring3 :", myintro.find(substring3)) #it shows -1


#replace the Word -----vayena run 
intro = "Im Adhish pokharel and I like learning Python"
new_intro = intro.replace("python", "java")
print(new_intro)

#split the Sentence
intro_new = intro.split() 
print("after split :", intro_new)

