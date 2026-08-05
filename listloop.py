#####Looping Through Lists ####

#Print every item using a for loop.
name = ["roshan", "ram", "Shyam", "Gita", "Rita","bishnu", "Mukunda", "Pashupati"]
for x in name:
    print(x) 

#using While loop
print("After this While loop's ans")
i = 0
while i < len(name):
    print(name[i])
    i = i+1

#Print only even numbers.
num = [42,423,55,322,600,2,6,7,13,67,93,98,48]
evn_num = [nu for nu in num if nu % 2 == 0]
print("Even numbers: ", evn_num)


#Print only odd num

odd_num = [odnm for odnm in num if odnm % 2 != 0]
print(odd_num)


#count the  num of elements
count = len(num)
print("NUm of elements in Number's List : ", count)



#Find the largest number.
largest = max(num)
print(largest)


#Find the smallest number.
smallest = min(num)
print(smallest)


#Calculate the sum of all numbers
total = sum(num)
print("Sum of all elements: ", total)


#calculate the Average of numbers
average = sum(num) / len(num)
print("Average : ", average)



#Print item in reverse order
print("Ordered list: ", num)
print("Reversed order: ", num[::-1])