####Tuple#####
"""
tuple are used to store multiple items in a Single variable

"""
#Qn.1 __
"""Create a tuple conatain the names of six countries..
    write a program to::
    1.print the first element
    2.print the last element
    3.print the fouth element
    4.print the elements from index 2 to index 4 using slicing

"""
countries = ("Nepal", "India", "Pakistan", "Bhutan","japan")
print("First element: ", countries[0])
print("last element: ", countries[-1])
print("fourth element: ", countries[3])
print("First element: ", countries[0:5])


#Qn. 2
"""Create a tuple containing five programming languages. Write a program to:
    1.Add a new programming language to the tuple.
    2.Remove one existing programming language from the tuple.
    3.Print the updated tuple.

"""
pro_lang = ("Python", "Java", "CSS", "C++", "HTML")
print("Before adding new language::", pro_lang)

#convert tuple into list
new_lst = list((pro_lang))
print(new_lst)

#Adding a lang..
new_lst.append("Go")
print(new_lst)

#removing the lang..
