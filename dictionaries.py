###Python Dictionaries
"""
dictionaries are used to store data value in key:value --pairs/form
1. Ordered
2.Changable
3.Do not allow Duplicates

"""

thisdict = {
    "name" : "Adhish",
    "age" : 19,
    "DOB" : 2007_7_16
}
print(thisdict)
print(thisdict["age"])

#Duplicates not allowed
values = {
    "frns" : "pratik",
    "hmch" : 3,
    "bstf" : "Bimal",
    "frns" : "Nazim"
}
print(values) #its replace the pratik with Nazim 
                # cuz it's not allow dupliacte value

print(len(thisdict))
print(len(values)) #variables are 4 but it's 3 cuz one value is Duplicate 


##IN dictionary items can be of any data type:
