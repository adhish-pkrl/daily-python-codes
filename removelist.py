#Removing List Items

#Remove an item using remove().
lst = ["Apple", "Banana", "Mango"]
lst.remove("Banana")
print(lst)

#Remove an item using pop().
let = ["Apple", "Banana", "Mango","Orange"]
let.pop(2)  #Mango will be remove
print(let)  

#last item without specifying an index.
let.pop(-1) #Orange will be remove
print(let)

#Delete an item using del.
del let[0]  # Delete first item (Apple)
print(let)

#Clear the entire list.
lst.clear()
print(lst)

#Remove all duplicate elements.
lists =[1,4,6,7,8,5,42,2,7,8,1,4,74,4,5,8,42]
final_list = list(set(lists))
print("Items With Duplicate value: ", final_list)



#Remove all even numbers.
lists = [nm for nm in lists if nm % 2 != 0]
print("without even: ", lists)


#remove odd numbers 
lis = [1,4,6,7,8,5,42,2,7,8,1,4,74,4,5,8,42]
lis = [mn for mn in lis if mn %2 == 0]
print(lis)


#Remove a specific student name.
name = ["roshan", "ram", "Shyam", "Gita", "Rita","bishnu", "Mukunda", "Pashupati"]
name.remove("ram")
print(name)

#Remove an element by index.
name.pop(3)
print(name)


#Explain the difference between remove(), pop(), del, and clear().
"""
remove() --> 
"""