###Chapter 7
#7.1 Mathmetical Functions\

#Square Root of element
import numpy as np
arr = np.array([4,9,16])
print("Square root:",np.sqrt(arr))

#power 
print("Power:",np.power(arr, 2))\

#Exponential
print("Exponential:", np.exp(arr))

#Natural log
print("Log:",np.log(arr))

#Absolute Value
print("Absolute value:", np.abs(arr))




##Statistical Functions 
import numpy as npp

#mean() - Agerage
marks = npp.array([70,35,60])
print("Mean:", np.mean(marks))

#median() - Middle value
print("Median:", np.median(marks))

#Std() - Standard Deviation
"""

"""
print("Standard deviation:", np.std(marks))

#var() -Variance
"""

"""
print("Variance:", np.var(marks))

#min() & max() - Minimum and Maximum
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))



###Percentiles
"""
Percentile भन्नाले कति प्रतिशत डेटा भन्दा तल वा बराबर 
    मान पर्छ भन्ने कुरा जनाउँछ।
"""
sales = npp.array([1000,2000,4000,6000])

print("25 percentile:",np.percentile(sales, 25)) #25th percentile
print("50th per/ medina:",np.percentile(sales, 50)) #50th percentile/  Median
print("75th Percentile:",np.percentile(sales, 75)) #75th Percentile



##Correlation Coefficient
"""
Correlation coefficient भन्नाले दुईवटा भिन्न (variables)..
    बीचको सम्बन्ध कस्तो छ भनेर मापन गर्ने संख्यात्मक मान हो।
यसको मान सधैं -1 देखि +1 बीचमा हुन्छ।
"""
sales = np.array([100,200,300,400])
advertisement = np.array([10,20,300,40])
print("Correlation Coefficient:",np.corrcoef(sales, advertisement))

x = np.array([1,3,5,7])
y = np.array([70,60,50,10])
print("neg corrcoe:", np.corrcoef(x,y))

x3 = [1, 2, 3, 4, 5]
y3 = [7, 3, 9, 2, 8]
print("No relation corrcoe:", np.corrcoef(x3,y3))



#Covariance
"""
Covariance measures how two variables change
 together. Positive means they move in the same
   direction, negative means opposite, 
    near zero means no clear relation.
"""
x1 = np.array([1,3,5,7])
x2 = np.array([4,6,8,10])
print("Covariance:", np.cov(x1,x2))



#Real life Example..->
##Daily revenue:
revenue = np.array([2000, 3000, 2500, 4000, 3500])
#Analysis:
print("Average Revenue:", np.mean(revenue))
print("Highest Revenue:", np.max(revenue))
print("Revenue Spread:", np.std(revenue))
print("Top 90% Revenue Threshold:", np.percentile(revenue, 90))
