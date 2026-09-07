##Array shape
"""
the shape of an array is the number of element..
    in each dimension
"""
import numpy as np
arr = np.array([[1,42,46,55],[5,9,43,24]])
print(arr.shape)


#modify the dimension
ary = np.array([1,2,3], ndmin = 6)

print(ary)
print("Shape of an array: ", ary.shape)



print("After this Re-shape array!")
###Array Re-shape
"""
Re-shaping means Changing the shape of an array.
"""



# 1D to 2D
aryy = np.array([1,2,3,4,5,6,7,8])
newary = aryy.reshape(2,4)
print(newary)
newar = aryy.reshape(4,2)
print(newar)




# 1-D to 3-D 
aray = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newaray  = aray.reshape(2,3,2) 
####### 2 --> 2block hunii
#       3 --> each block has 3 rows
#       2 --> each row has 2 element
print(newaray)
print(newaray.ndim)




###Return Copy or View
arayy = np.array([1,2,3,4,5,6,7,8])
print(arayy.reshape(4,2).base)  #base leyy yo data just copy ho vanera inform garxa




print("After this Flattening the array.")
##Flattening the array
"""
Flattening array means converting 
    a multidimensional array into a 1D array
"""

aryea = np.array([[4,6],[8,10]])
print(aryea)
newarray = aryea.reshape(-1)
print("Changes into 1-D:",newarray)





print("After this Array Iterating..!")
aery = np.array([100,102,103])

for x in aery:
    print(x)


#Iterating 2-D array
arrey = np.array([[104,105,106], [204,205,206]])

for y in arrey:
    print(y)



print("Print's each element: ")
#iterate in each scalar element of 2-D array:
newarrayy = np.array([[404,405,406],[505,506,507]])

for z in newarrayy:
    for a in z:
        print(a)




#3-D array iterating to print each element 
araaaa = np.array([[[111,222,333], [444,555,666],[777,888,999]]])
print(araaaa.ndim)

for b in araaaa:
    for c in b:
        for b in c:
            print(b)




print("After this Using nd....()")
#using nditer()
for g in np.nditer(araaaa):
    print(g)



for idx, n in np.ndenumerate(newarrayy):
    print(idx, n)






print("After this Joining array")
#joining the array
"""
joining means putting contents of two or more arrays
     in a single array
"""

arr1 = np.array([1,2])
arr2 = np.array([4,6])

jarray = np.concatenate((arr1, arr2))
print(jarray)
joinarr = np.stack((arr1,arr2), axis = 1)
print("Axis 1 in 1-D array:",joinarr)


#join two 2-D array along rows (axis = 1):

arr11 = np.array([[33,22],[66,77]])
arr12 = np.array([[88,11],[00,99]])

jonarr = np.concatenate((arr11,arr12), axis= 1)
print(jonarr)




##Stack along Rows
joiningarr = np.hstack((arr1,arr2))
print("Stack along rows/ prints on same row:",joiningarr)


joiningarray = np.vstack((arr1,arr2))
print("Stack along columns: ",joiningarray)


#dstack 
stackarray = np.dstack((arr1,arr2))
print("d-stack:", stackarray)

a1= np.array([999,888,777])
a2 = np.array([111,222,333])

star = np.dstack((a1,a2))
print("It changes into 3d array",star)
