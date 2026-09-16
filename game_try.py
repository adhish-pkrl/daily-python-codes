
import numpy as np

from numpy import random
x = random.randint(100)

#Taking input from user

for i in range(10):
    u_num = int(input("guess the number: "))
    if x == u_num:
        print("did it")
        break
    else:
        if u_num >= x:
            print("The num is lesser then", u_num)
        else:
            print("The num is grater then", u_num)
        print("try again")
print("the num is:", x)

# players = ["bipen", "Bibek", "Pratik", "Ankit", "Sujal"]

# for x in players :
#     print(x)
#     if x == "Bibek":
#         print("Name found")
#         break
# # for x in range(len(players)):
# #     print(players[x])

# # i = 0 
# # while i < len(players) :
# #     print(players[x])
# #     i = i +1


