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

"""
#Append user input to a list.
index = int(input("Enter the index to upadete the value: "))

nw_name = input("Enter the new name: ")
names[index] = nw_name
print("Updated list : ", names)

"""

###Add another list to an existing list.
lst = ["Apple", "Banana", "Mango"]
new_lst = ["Sweet", "Healthy"]
#combine list
com_lst = lst + new_lst
print("Combined list :", com_lst)


#Insert multiple values.
com_lst[2:2] =["krishna", "Gopiram", "Ujwal"]
print(com_lst)


#added item in Nested list
nst_list =[
    ["hari", "Hero", "talented"],
    ["Ram", "Nice", "Intermediate"]
]

nst_list[0].append("Smart")
print(nst_list)

#if need to add new person 
nst_list.append(["Rita", "kind", "Biginer"])
print(nst_list)


#Create a shopping list and keep adding items.
# shoping_list = [

# ]
# print("Add your Shopint items: ")
# while True:
#     item = input("Add your Item:")

#     if item.lower() == "stop":
#         break

#     shoping_list.append(item)
#     print(f"'{item}' has been added to your shoping list.")
# print("\nFinal Shoping List: ", shoping_list)


#Add numbers until the user enters 0.
# numbers = [

# ]
# print("Bro add your numbers: ")

# while True:
#     num = int(input("Add your numbers:"))

#     if num == 0:
#         break

#     numbers.append(num)
#     print("Succesufully you added the numbers")
# print("\n Funal Numbers: ", numbers)




#Compare append(), extend(), and insert()

"""
append() --> add the item at the last of the List.

extend() --> adds multiple items from iterable.

insert() --> insert the one item at a specific position.
"""

#append
fruits = [
    "apple", "banana"
]
fruits.append(["graps", "orange"])
print(fruits)


#extend
fruits.extend(["Mango", "grape"])
print(fruits)

#insert
fruits.insert(1, "Papaya") #index 1 ma add hunxa
print(fruits)


