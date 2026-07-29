# #String 

# print("This is String and its written in Single or double Quets")

#(Starting , ending)
text = 'Adhish'
print(text[0])
print(text[0:3])  #yesma Last ko Index mathii ko value Print hunna 

fruits = ["apple", "banana", "cherry"]
print(fruits[0])

print(text[:])   # ' : ' yo ley Starting ra ending laii Xuttai garxa
print(text[4:])   # ' : ' yo ley Starting ra ending laii Xuttai garxa
print(text[:6])   # ' : ' yo ley Starting ra ending laii Xuttai garxa
print(text[1:-3])  #Negative Indexing 


# #UPPER case

first_name = "  AdhISh  "
print(first_name.title())
print(first_name.upper())
print(first_name.lower())


# #Remove Whitespace

# ####White sapce is a space between and/or after the actual text
second_name =" Adhish , Pokharel"
print(second_name.strip())
print(second_name.upper().strip())  #aaghii Poxi ko White space lai clean garxa


#replace method 
print(first_name.replace("Ad", "ww")) #case sensitive hunxa so j xa name ma spelling tei huna parxa replace garda

print("Spliting Strin :", second_name.split(",")) #, ko aadhar maa XuttauXAah (split garxa)
print("Spliting Strin :", second_name.split())    # space ko aadhar ma hunxa 
print("Spliting Strin :", second_name.count(second_name))

#check byy my self String methods and Click on Links 

#String Concatenation 
a = "Frist hero"
b = " last hero"
c = a + b
print(c)


#formating String 

name = "Adhish"
score  = 45
str = f"The score of {name} is {score} "
print(str)



#Escape Character 
print("My name is \"Adhish\" Pokharel ")   #yesma error aauxa CUZ String vitra Double Quotes use Unvalid hunxa

print("My name is \"Adhish\" Pokharel")   


#voli boolean 
