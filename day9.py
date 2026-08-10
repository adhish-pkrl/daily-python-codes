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


