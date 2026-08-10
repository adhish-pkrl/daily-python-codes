###Dictonaries
"""
{
keys : values
}
items

"""
user = {
    "name" : "Adhish",
    "age" : 19
}
for x in user:
    print(x) #it prints keys
    print(user[x])

for y in user.values():
    print(x)

print(user[x]) ##value print garxa same mathi jasteii

#change Keys and values
user["name"] = "Pratik"
print(user)

#remove
user.pop("name")
print(user)
user.popitem()
print(user)


#Add the valuess and items



#LOOP
for x in user.keys():
    print(x)

for z in user.values():
    print(z)

for m in user.items():
    print(m)


########Self Learning after class#######
lst = {
    "name" : "Aadhu",
    "age" : 19,
    "level" : "bachelors",
    "jnYear" : 2025
}
print(lst)

##dictonaries items
print(lst["jnYear"])


#duplicates are not allowed

#length
print(len(lst))

##Dictonary Items -Data Types
"""
The values in dictonaries can be of any data type
"""
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"], ###Can be List
  "fav0" : {1,3,4,6,88,864}, ###Can be set
  "modles" :("Purano", "Mid year", "New Model") ##Can be tuple
}
print(type(thisdict))

ktaharu = dict(member ="John", age=36, country = "Africa")
print(ktaharu)


#get the value of brand key:
print(thisdict["brand"]) #key ko value nikalniii

print(thisdict.get("year"))

##Print the list of Keys
print(thisdict.keys())




#Add a new item to the original Dictonary
car ={
    "brand" :"BMW",
    "Model" : "i7 Sedan",
    "Year" : 2017
}
x = car.keys()
print(x) #before adding the new key 

car["color"] = "Blue"
print(x)  # after change

###  Get Values
print(car.values())

###  Get items ##
print(car.items())


#  Check the Key is Exist or not
if "year" in lst:
    print("Yes this model is one of the keys in the lst dictionary")
else:
    print("pak")

if "Model" in car:
    print("Yesh it exists")
else:
    print("No this is not")
