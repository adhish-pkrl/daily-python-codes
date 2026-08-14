###IF-Elif-else

#grade calculator 
marks = float(input("Enter your marks: "))
if marks >=90:
    print("A+")
elif marks >=80:
    print("A")
elif marks >=70:
    print("B")
elif marks >=60:
    print("C")
elif marks >=40:
    print("D")
else:
    print("F")


#Age Category      ###--?>Wrong xaaa
age = int(input("Enter your age: "))
if age >12:
    print("Child")
elif age >19:
    print("Teenager")
elif age >59:
    print("Adult")
else:
    print("Senior Citizen")
