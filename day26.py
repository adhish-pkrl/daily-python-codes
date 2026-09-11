import pandas as pd
print(pd.__version__)


student = ['A','B','C','D']
print(student)

print(pd.Series(student))
srs  = pd.Series(student)
#label
print(srs[1])




students = {
    "name" : "Adhish",
    "age": 19
}
print(students)

#pandas ko data frame is 2D array 
    #prints as a Table
# record = pd.DataFrame(students)
# print(record)
# record.head()


###Self learn
"""

read jason
sammaa//\
"""