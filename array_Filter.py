##NumPy Filter Array
"""
getting some elements out if an existing array and,,
    creating a new array out of them is called filtering

*  
"""
import numpy as np
arr = np.array([1,2,4,5,6])
x = [True, True, False,True, False]
newarr = arr[x]
print(newarr)



#filter in array for even numbers
ary = np.array([2,3,5,7,8,10])
print("Unfilted array:", ary)
flt = []
for element in ary:
    if element %2 == 0:
        flt.append(True)
    else:
        flt.append(False)
print("prints t/f : ",flt)
filtered_array = ary[flt]
print("Filtered array: ", filtered_array)




#using vactorization 
print("After this Vactorazation-->")

sales = np.array([400,500,700])
with_Vat = sales * 0.13 + sales
print("With vat Price: ", with_Vat)





#vactorization for array: -->
aryy = np.array([20,70,67,35,97,100])

new_arr = []
flt_arr = aryy % 2 ==1

print(flt_arr)
ft_array = ary[new_arr]
print(ft_array)



