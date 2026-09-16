
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

# import numpy as np

# from numpy import random
# x = random.randint(5)

# #Taking input from user

# user_arr = ([])

# for i in range(5):
#     u_num = int(input("guess the number: "))
#     if x == u_num:
#         print("did it")
#         break
#     else:
#         print("try again")
# print("the num is:", x)
# if x == user_arr:
#     print("DID it")
# else:
#     print("Vak")
    # if x == user_arr:
    #     print("You guessed it right")
    #     break
    # else:
    #     print("Try again")
    #     if x == u_num:
    #     print("You did it")
    # else:
    # print("Try again")

# print("The num is:", x)
