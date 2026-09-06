##Array Shape
"""
Important topic
"""
import numpy as np
arr = np.array([[1,3],[4,7]])
print(arr)
print(arr.shape) #How many rows ans How many columns (2--row, 4--column)

print(arr.size)  #sabei vitra element kati xa vaneko 



#reshaping means changing the shape of an array.
arry = np.array([1,3,5,6,8,9,2,10,11])
newarr = arry.reshape(3,3)
print(newarr)
#used in EDA --Data clean , data ?, how many rows ?, how many cloumns ?


#array loop
for x in arry:
    print(x)

ary = np.array



#Joining in numpy
#joining means putting contents for two or more array in a Single array
arr1 = [2,4]
arr2 = [7,8]
print("plus:",arr1+ arr2)


#concatenate
concarr = np.concatenate((arr1, arr2))
print("concatenate :",concarr)


import numpy as npp
arry1 = npp.array([2,4])
arry2 = npp.array([7,8])
first_name = npp.array([["Adhish", "Pratik", "Sujal"]])
last_name = npp.array([["Pokharel", "Poudel", "Shrestha"]])

full_name = npp.concatenate((first_name, last_name))
print(full_name)
full_name = npp.concatenate((first_name, last_name), axis = 1)
print(full_name)



####new example
matrix = npp.array([[2,4], [6,8]])
print(npp.sum(matrix))
print(npp.sum(matrix, axis=0)) #axis = 0 -- rows
print(npp.sum(matrix, axis=1)) #axis = 1 -- column


#hstack self study 
#vsteck self  study
#dsteck self study
