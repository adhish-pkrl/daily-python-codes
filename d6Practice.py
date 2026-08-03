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


