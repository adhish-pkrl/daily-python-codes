##numpy 
import numpy as np
numbers = np.array([2,3,4,5])
result = numbers * 2
print("mul by 2: ", result)


# to print total Sales
sales = np.array([200,400,670,930])

#calculate
total_sales = np.sum(sales)
print("Total sales : ", total_sales)

#Shape of array how many rows & columns
print("Shape ",sales.shape)

#size of array -> Total num of elements in array
print("TOtal elements inside array:",sales.size)

#data type of elements inside array
print("Data type of elements inside array:",sales.dtype)


#change the data type of an array
arr = np.array([5,6,7], dtype= float)
print(arr)
print("Data type of elements inside an array:", arr)
arr = arr.astype(int)
print("Again change it into int: ",arr)



##Arrange 
ary = np.arange(1,10)
print(ary)

aryy = np.arange(1,20,4)
print(aryy)



aray = np.eye(3)
print(aray)


##Boolean Indexing
arryyy = np.array([10, 20, 30, 40, 50])

print(arryyy[arryyy > 25])




#Fancy indexing 
arya = np.array([10,20,30,40,90,75])
print(arya[[0,2,4]])



##Convert any array like 3-d, 2-d to 1-d
arr1 = np.array([[27,89,33,67], [66,88,23,11]])
flat = arr1.flatten() #Copy function
print(flat)

flat = arr1.ravel() #Copy function
print(flat)