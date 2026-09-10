##Mathematical & Statiscs
"""

"""
#Statistical Functions
#mean
import numpy as np

marks = np.array([50,40,70])
print(np.mean(marks))
print(np.std(marks))

"""
how far a set of numbers are 

SD -> is the square root of the variance
Variance -> is the square of the SD

SD ley data mean bataw kati tada xa vanera dinxa
So variance ley pani same same but Diffelent haha

"""
print(np.var(marks))
print(np.sqrt(155.55555555555554))


#min and max
print(np.max(marks))
print(np.min(marks))




#percentile
"""
Percentile 
"""
print(np.percentile(marks, 25)) 
print(np.percentile(marks, 50)) #Q2
print(np.median(marks))



print("After this Coreelation Coefficient-->")
###Coreelation Coefficient

sales = np.array([100, 200, 3000, 400])
advertising = np.array([10, 20, 10, 40])

print(np.corrcoef(sales, advertising))




