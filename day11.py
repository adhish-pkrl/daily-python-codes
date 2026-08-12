###nested if ###
"""
if statement inside another if statement

"""
x = 32

if x > 10:
    print("above 10")
    if x > 20:
        print("below 20")
    else:
        print("but not above 20")
else:
    print("smaller than 10")


###Assignment
"""
scholarship pauna lai eligilible xa ki nei check garni

marks > 90
attendence > 80
income source < 20k / month

"""
marks = int(input("enter your marks"))

attendence = int(input("enter your attendence:"))

income_src = int(input("enter your encome socrce"))

if marks > 90:
    if attendence > 80: 
        if income_src < 20000:
            print("you are eligible for scholorship")   
        else:
            print("your income is too high")
    else:
        print("your attendence is not enough")
else:
    print("your marks is not enough")

