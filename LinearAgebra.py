##linear Algebra for Data Analysts
"""
Used in
    *Machine learning
    *Recommendation Systems
    *Image Processing
    *Optimization Problems
    *Data Transformations

"""
#Dot product
"""
the dot product multiplies corresponding
    and adds them
"""
import numpy as np
arr1 = np.array([1,3,5])
arr2 = np.array([9,8,7])
print("Dot pro:",np.dot(arr1,arr2))


##Matrix Multiplication
a = np.array([[2,4],[7,9]])
b = np.array([[2,6],[5,4]])
print("Matrix mul:", np.matmul(a,b))


#Determinant
arr = np.array([[1,2], [3,4]])
print("Determinant:", np.linalg.det(arr))

#inverse
print("Inverse:", np.linalg.inv(arr))




##Solving Linear Equation
"""
2x + y = 5
x + 3y = 6
"""
A = np.array([[2,1],[5,6]])
B = np.array([5,6])
print("Linear solve:", np.linalg.solve(A,B))



A1 = np.array([[2, 0],
              [0, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A1)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)




#Nan
"""
not a number
"""
arr11 = np.array([10, 20, np.nan, 40,50])

print(arr11)

print(np.isnan(arr11))
print(np.sum(np.isnan(arr11)))


##Removing Missing values
clean_arr = arr11[~np.isnan(arr11)]
print("Cleaned array:",clean_arr)



##replacing missing values
mean_value = np.nanmean(arr11)
arr11[np.isnan(arr11)] = mean_value
print(arr11)


###using where() 
marks = np.array([45,60,30,80])
result = np.where(marks >50, "Pass", "Fail")
print("Student marks only:", marks)
print("Student marks result:",result)



##Supermarket Cleaning
# revenue = np.array([2000,3000,np.nan, 4000, 0])
# #replace missing with average
# revenue = [np.isnan(revenue)] = np.nanmean(revenue)

# #replace zero revenue with minimum valid revenue
# min_valid = np.min(revenue[revenue>0])
# revenue[revenue == 0] =min_valid
# print(revenue)

revenue = np.array([2000, 3000, np.nan, 4000, 0])
#Step 1: Replace missing with average
revenue[np.isnan(revenue)] = np.nanmean(revenue)
#Step 2: Replace zero revenue with minimum valid revenue
min_valid = np.min(revenue[revenue > 0])
revenue[revenue == 0] = min_valid
print("cleaned data:",revenue)



#combined multiple Conditions
sales = np.array([1000,3000,5000,2000])
high_sales = sales[(sales> 2000) & (sales < 6000)]
print("High sales:",high_sales)



##10 