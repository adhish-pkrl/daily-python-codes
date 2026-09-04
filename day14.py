##pattern printing 
for i in range(1,7):
    for j in range(7-i):
        print(j, end = "")
    print()

# """
#     *
#    **
#   ***
#  ****
# *****
# """
for i in range(1,6):
    for j in range(5-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end = " ")
    print()

        # for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end="" )
#     for j in range(i):
#         print("*",)
 
for i in range(1,7):
    for j in range(7-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end = " ")
    print()

"""
*****
****
***
**
*
"""
for i in range(6):
    for j in range(5-i):
        print("*", end = " ")
    print( )

"""
****
"""
