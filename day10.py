#### IF else Condition ####
"""
Supports the usual logical conditions from mathmathmatics

"""
"""if condition :
       result 
       
"""

a = 99
b = 8
if a > b :
    print("a is grater then b")
else :
    print("b is grater then a ")

###   multiple if conditions
marks = int(input("enter your marks"))
if marks > 90:
    print("You have Got A plus")
elif marks > 80:
    print("You got A")
elif marks > 70:
    print("you got B+")
else:
    print("You just passed")



##Indentation

##password entry 
password = "nepal@-123"
enter_pass = str(input("Enter your password:"))
if enter_pass ==  password:
    print("welcome back")
else:
    print("Not matched")



## using loop to check pass fail
# mar = [34,53,23,76,78,97,23,88,44]
# for i in mar:
#     passed = i if i >=40 else "failed"
#     print(passed)

mar = [34,53,23,76,78,97,23,88,44]
# jpt = [i for i in mar if mar >=40]
# print(jpt)
passed_mrks = []
failed_mrks = []

for m in mar:
    if m >=40:
        passed_mrks.append(m)  ##passed marks matrei save garxa
    else:
        failed_mrks.append(m) ##failed marks matrei store garxa
print(passed_mrks)
print(failed_mrks)


## using one line condition 
flmr=[]
for x in mar :
    print(x, "passsed" if x>=40 else "failed")


##Tomorrow ==nested if