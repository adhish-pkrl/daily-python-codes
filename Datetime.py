###Dates
"""
a date in python is not a data type of its own,
    but we can import a module named datetime
"""
import datetime

x = datetime.datetime.now()
print(x)

#Return the Year and Name of Weekday
print(x.year)
print(x.strftime("%A"))


#creating date Objects
z = datetime.datetime(2020,5,17)
print(z)
