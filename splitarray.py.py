####NumPy Splitting Array
"""
splitting is reverse operating of joining 
..Splitting breaks one array into multiple
"""
import numpy as np
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 3)

print(arr)

print(newarr)

nwarr = np.array_split(arr, 4)
print(nwarr)


#access splited array using index
nwarray = np.array_split(arr, 3)
print("This is the new array elements:",nwarray)
print("index 0 array: ", nwarray[0])
print("index 1 array: ", nwarray[1])
print("index 2 array: ", nwarray[2])


##split the 2-D array
import numpy as nnp
ary = nnp.array([[23,45,67], [10,20,30], [31,13,68], [909,808,707], [4, 5, 6], [7, 8, 9]])

nwTDar = nnp.array_split(ary, 4)
print("normal 2-D array:",ary)
print("After slicing:", nwTDar)

##2-D array into three 2-D arrays along columns
new2darr = np.array_split(ary, 3, axis = 1)
print("Along Columns: ", new2darr)



#using hsplit()
new2darray = np.hsplit(ary, 3)
print("using hsplit():",new2darray)

# nw2dar = np.vsplit(ary, 4)
# print("using vsplit():", nw2dar)
# Create a 2D array (4 rows, 2 columns)
arry = np.array([[1, 2],
                [3, 4],
                [5, 6],
                [7, 8]])

# Split into 2 equal parts vertically
result = np.vsplit(arry, 2)

# Print each part
for part in result:
    print("Using vsplit(): ",part)