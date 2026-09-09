##Array Filter
"""
elements out of existing array and creating a new array
    A boolean index list is a list bollean,,
    corresponding to the array index
"""

import numpy as np
arr = np.array([1,2,4,5,6])
print(arr)
x = [True , False, True , False, True]
newarr = arr[x]
print(newarr)



#Filter in List
lis = [2,5,7,8,9,10]
flt = []
for i in lis:
    if i % 2==0:
        flt.append(i)
print("Filtered array: ",flt)




#Filter in array
ary = np.array([2,4,6,8])
print(ary)
filt = []
for element in ary:
    if element % 2 ==0:
        filt.append(True)
    else:
        filt.append(False)
print(filt)
filtered_arr = ary[filt]
print(filtered_arr)




#Vactorazation 
"""
performing operation on entire array at once..
     without using python for loop
kunei array ma operation perform garni without loop
"""
# sales  = [ 100,200,300]
# withvat = []
# for j in sales:
#     j * 0.13 + i: --> that's we use loop !!

print("Using vactorazatioin")
sales = np.array([100,200,300])
withvat = sales * 1.13
print(withvat)