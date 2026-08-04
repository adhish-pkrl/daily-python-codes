##While loop
"""
with While loop we can execute a set of statement as long as a condition is True
"""
a = 2
while a < 6 :
    print(a)
    a = a+1

# #break 
# i= 1
# while i < 7:
#  print(i)
#  if i == 5:
#     break
# i = i+1
print("After this using break")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue statemeent
p = 0
while p < 8:
   p += 1
   if p == 6:
      continue
   print(p)  #6 won't print cuz of continue statement
print("After this it's else ")
###Else /////
##--> else is used to print a message once the condition is false

c = 1
while c < 9:
   print(c)
   c = c+ 1
else:
   print(" c is no longer than 9")


##For loop 
frindss = ["Adhish", "pratik", "Sujal", "Amrit", "Prasun"]
for x in frindss: 
   print(x)

#for each string
for y in "Adhish":
   print(y)


#Break 
for x in frindss:
   print(x)
   if x =="Sujal" :
      break

#continue
print("After this Continue Statement")
#frindss
for u in frindss:
   if u =="pratik":
      continue
   print(u)

#range function
for y in range(4):
   print(y)

for a in range(2, 6):
   print(a)


#Else in for Loop
print("After this \'else in loop \'")
##
for x in range(6):
   print(x)
else:
   print("finally finished!")

