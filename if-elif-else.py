###IF-Elif-else

# #grade calculator 
# marks = float(input("Enter your marks: "))
# if marks >=90:
#     print("A+")
# elif marks >=80:
#     print("A")
# elif marks >=70:
#     print("B")
# elif marks >=60:
#     print("C")
# elif marks >=40:
#     print("D")
# else:
#     print("F")


# #Age Category      ###--?>Wrong xaaa
# age = int(input("Enter your age: "))
# if age < 12:
#     print("Child")
# elif age <19:
#     print("Teenager")
# elif age < 59:
#     print("Adult")
# else:
#     print("Senior Citizen")




# #Number Type
# num = int(input("enter a num: "))
# if num > 0:
#     print("NUm is Positive")
# elif num < 0:
#     print("Num is negative")
# else:
#     print("Zero")



# #Traffic Light 
# signal = str(input("Enter a traffice Light Color: "))
# light = signal.lower()
# if light == "red":
#     print("Stop !!")
# elif light == "yellow":
#     print("Wait")
# elif light == "green":
#     print("Go")
# else :
#     print("Invalid Signal")



# #Day of the Week
# day = int(input("Enter the day (1-7): "))
# if day == 1:
#     print("Sunday")
# elif day ==2:
#     print("Monday")
# elif day ==3:
#     print("Tuesday")
# elif day ==4:
#     print("Wednesday")
# elif day ==5:
#     print("Thrusday")
# elif day ==6:
#     print("Friday")
# elif day ==7:
#     print("Saturday")
# else: 
#     print("Invalid day")




#Simple Calculator
nm1 = int(input("Enter a 1st number: "))
nm2 = int(input("Enter a 2nd number: "))
operator = input("Choose a Operator(Add, Sub, Mul, Div) : ")
optr = operator.lower()
if optr == "add":
    print(nm1 + nm2)
elif optr == "sub":
    print(nm1 - nm2)
elif optr == "mul":
    print(nm1 * nm2)
elif optr == "div":
    print(nm1 / nm2)
else:
    print("Invalid Operation")
