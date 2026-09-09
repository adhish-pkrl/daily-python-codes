###NumPy Searching Arrays
"""
we can search an array for a certain value, and return the indexes that get a match

"""

#find the index where the value was found--
import numpy as np
arr = np.array([2,3,4,5,6,7,8])

x = np.where(arr ==5)

print("Index of value 4: ", x)



#find the indexes where the value are odd--

arry = np.array([10,15,20,40,47,98,101])

y = np.where(arry%2 == 1)
print("Odd value indexes: ", y)

#values are even
z = np.where(arry%2 == 0)
print("index of even value: ", z)






print("After this SearchSorted! ->")
###Search Sorted 
"""
there is a method called searchsorted(),
    which performs a binary search in the array
"""
import numpy as nnp

arra = nnp.array([6,7,8,9])
a = nnp.searchsorted(arra, 7)
print("num 7 should is sort in index:",a)

b = nnp.searchsorted(arra, 10)
print("10 should be sort in index: ", b)


##Search from the right Side--
ary = nnp.array([6,8,9,10])
d= np.searchsorted(ary, 7, side= 'right')
print("7 sort form right side:",d)




#sort multiple values-->
sarr = nnp.array([1,3,6,9])
f = nnp.searchsorted(sarr, [2,5,10])
print("Multiple value sort: ",f)