#NumPy
#What is NumPy
"""
NUmmpy is the fundamental package.
 for scientific computing in Python.

1.It is a python library that provides..
    a multidimensional array object.

"""
#conversion from other python structures(i.e lists and tuples)
#replacing, joining, or mutating existing arrays



#1D array Creation 
import numpy as np
arr = np.array([0,1,2,3,4,5,6,7,8])
print(arr)

#test 
# np.arange(10)
# ary = np.array([1,2,3,7,43,4,4,2,3,6])
# print(ary)
# np.arange(2,5,1)
# print(ary)
print(np.__version__)



###NumPy ndarray Object
"""
numPy is used to work with arrays.
    the array object in numpy is called ndarray
"""
print(arr)
print(type(arr))


#Dimensions in Array
#A dimension in array is one level of array depth(nested arrays).


# 0- D array
import numpy as nmp
zroD = nmp.array(23)
print("THis is the 0-D array: ", zroD)


#1-D array
#AN array has 0-D arrays as its element is called uni-dimensional or 1-D array
import numpy
exm = numpy.array([1,2,3,4,5])
print("example of 1-D array:",exm)


#2-D arrays
# An array that has 1-D array as it's elements is called a 2-D array
import numpy
twoD = numpy.array([[12,23,34,56],[78,89,90,10]])
print("Example of 2-D array: ", twoD)


#3-D arrays
#an array that has 2-D array as it's element is called 3-D array
import numpy as numppp
thrDv = numppp.array([[["Hur", "Fur","Churr", "Murr"], [2,4,6,8], ["Hari", "Ram", "Shyam","Puskar"]]])
print(thrDv)

#check the number of dimensions?
print("0-Dimension array:",zroD.ndim)
print("1-Dimension array:",exm.ndim)
print("2-Dimension array:",twoD.ndim)
print("3-Dimension array:",thrDv.ndim)




#Higher Dimensional Arrays
#an array can have any number of Dimensions.
import numpy as pn
ayr = pn.array([1,2,3], ndmin=8)

print(ayr)
print("Number of dimension:", ayr.ndim)




######Access Array Element
print("After this Access array element--><><>>")

#1-D array 
import numpy as aa
od = aa.array([32,44,53])
print(od[1]) #44


#2-D array
import numpy as op
td = op.array([[2,4,6], [8,10,12]])
print("2-D element on 1st row: ", td[0,1])
print("2-D element on 1st row: ", td[0,2])


print("2-D element on 1st row: ", td[1,2])
print("2-D element on 1st row: ", td[1,0])



#3-D array 
import numpy as nump

threD = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(threD[0, 1, 2])


print("After this my test:")
# import numpy as np
# mytest = np.array([[[3,2,1], [6,5,4], [5,5,5]][[54,43,54,3],[343,5,43,4534,345,543],[66,77,88,99]]])
# # print(mytest[1,0,1])
# print(mytest.ndim)
# import numpy as nnpp

# are = nnpp.array([[[1,2],[4,0]],[[44,22],[66,77]],[[99,100],[00,11]]])
# print(are.ndim)





##Array Slicing
#taking element from one given index to another given index
# [start, stop, step/gap]
import numpy as qqw
we =qqw.array([1,32,87,0,998,0,45,23,65,768,34])
print(we[2:9:1])



#2-D array Slicing
import numpy as np

ayr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(ayr[1, 1:4])



#Data types in Numpy
import numpy as ss
ww = ss.array([2,4])
qq = ss.array(['apple', "banana"])
print(ww.dtype)
print(qq.dtype)

oo = ss.array([3,5], dtype='S')
print(oo)
print(oo.dtype)




print("After this Copy & view")
###Array Copy vs View
#the main diff btwn a copy and view of an array
# is that the copy is a new array,
# and the view is just a view of the original array

#####COPY
"""
make a copy, change the original array, and display both arrays:
"""
import numpy as uu
cpy = uu.array([43,3,23,24,556])
x = cpy.copy()
print(cpy)
# print(x)
cpy[0] = 42
print(x)
print(cpy)
print(x)
x[0]= 41
print(x)




####View
"""
make a view, change the view, and display both arrays:
"""
import numpy as jj
viw = jj.array([99,88,77])
y = viw.view()
print(viw)
print(y)
y[0] = 00
print("Changed in view: ", y)
print(viw)

viw[2]= 67
print(y)
print(viw)
#view
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)

#make changes in view
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# x[0] = 31

# print(arr)
# print(x)