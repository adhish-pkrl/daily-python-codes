###Adding List Items####

#Add one item using append().
names = ["Adhish", "Prarik", "prasun"]
names.append("Sujal")
print(names)

#Add multiple items using extend()
names.extend(["Bishal", "Rahul", "Bibek"])
print(names)


#inserting item in index 2
names[2] = "Bhuwan"
print(names)


#Append user input to a list.
index = int(input("Enter the index to upadete the value: "))

nw_name = input("Enter the new name: ")
names[index] = nw_name
print("Updated list : ", names)