##IF-Elif-else

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
if age < 12:
    print("Child")
elif age <19:
    print("Teenager")
elif age < 59:
    print("Adult")
else:
    print("Senior Citizen")




#Number Type
num = int(input("enter a num: "))
if num > 0:
    print("NUm is Positive")
elif num < 0:
    print("Num is negative")
else:
    print("Zero")



#Traffic Light 
signal = str(input("Enter a traffice Light Color: "))
light = signal.lower()
if light == "red":
    print("Stop !!")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else :
    print("Invalid Signal")



#Day of the Week
day = int(input("Enter the day (1-7): "))
if day == 1:
    print("Sunday")
elif day ==2:
    print("Monday")
elif day ==3:
    print("Tuesday")
elif day ==4:
    print("Wednesday")
elif day ==5:
    print("Thrusday")
elif day ==6:
    print("Friday")
elif day ==7:
    print("Saturday")
else: 
    print("Invalid day")




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




#Electricy Bill
unit = float(input("enter the Electricty Unit : "))
if unit < 100:
    print("Rs.5/unit")
elif unit < 200:
    print("Rs.7/Unit")
else:
    print("Rs.10/Unit")



#BMI category
BMI = float(input("Enter your BMI : "))
if BMI < 18.5:
    print("Under Weight")
elif BMI > 18.5 and BMI < 24.8:
    print("Normal")
elif BMI > 25 and BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")




#Shoping Discount
pur_amount = float(input("Enter perchase amount: "))
if pur_amount < 1000:
    print("No Discount")
elif pur_amount <4999:
    print("5% discount")
elif pur_amount < 9999:
    print("10% Discount")
else:
    print("20% Discount")




#ATM Withdrawal
username = "admin"
password = "1234"

#take a input
urname =str(input("Enter your username: "))
passwrd = str(input("Enter your password: "))
balance = 50000
if urname == username:
    print("Username matched")
    if passwrd == password:
        print("password matched")
        print("Login successful")
    else:
        print("passwrod not matched")
if urname == username and passwrd == password:
        amount = int(input("enter the amount: "))
        if amount  > balance:                print("Faild to withdrawal")
        elif amount % 5 == 0:
         print(f"withdrwal is valid {amount} ")
else:
    print("Enter valid Details!!!")





#Scholarship Eligibility
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))
income = float(input("Enter your family Income: "))

if age <= 25:
    print("Age is valid!")
    if marks >= 80:
        print("Marks valid ")
        if income < 500000:
            print("Valid income")
            print("you Got Scholorship !")
        else:
            print("Invalid income Scholorship faild")
    else:
        print("Invalid marks")
else:
    print("Invalid age!")




#Movie Ticket Pricing
age = int(input("enter your age: "))
movie_type = str(input("Enter the Movie type(premium/ normal) "))

if age < 12:
    print("Children RS.500")
    if age < 59:
        print("Adults RS. 250")
        if age > 60:
            print("Senior citizens RS.180")
            if movie_type == "premium":
                print("Extra charges Rs.100")
            else:
                print("Normal Ticket price")
        else:
            print("normal invalid age")
    else:
        print("Invalid age!")
else:
    ("not valid")







#Resturant Bill
food_bill = float(input("Enter the Price of bill: "))
num_of_ppl = int(input("Enter the numer of people: "))
if food_bill >= 5000:
    print("15 % Discount")
elif food_bill >=3000:
    print("10% Discount")
else:
    print("No discount")
each_person_paying_amount = food_bill / num_of_ppl
print(f"Each person Should pay {each_person_paying_amount}.! ")





#Employee Bonus
salary = float(input("Enter Your salary: "))
exprience = int(input("Enter your Years of Exprience: "))
performance_rating = int(input("Enter your performance rating: "))
if exprience > 2:
    print("You got a Bonus! of: ")
    if performance_rating >= 9:
        print("20%")
    elif performance_rating >= 7:
        print("10%")
    else:
        print("5%")
else:
    print("Your exprience is not valid for Bonus aajeii Kam gar Vaiii!!")






#Resturant Ordering System
food = str(input("Enter your Food (Burger, Pizza, Momo, Chowmein)"))
fod = food.upper()
room = str(input("enter Your Room Type(Standard, Deluxe, Suite): "))
night = int(input("Enter how many days you want to Stay: "))

if fod == "Burger":
    print(f"Price of {fod} Rs.225")
elif fod == "Pizza":
    print(f"price of {fod} Rs.510")
elif fod == "Momo":
    print(f"price of {fod} Rs.180")
else:
    print(f"price of Chowmein Rs.60")

if night >= 1 and night <= 2:
    print("Youll get No Discount!")
elif night >= 3 and night == 4 and night <= 5:
    print("Youll get Discount!")
else: 
    print("Youll get 15% Discount!")


if room == "Standard":
    room_type = room.upper()
    prcStrd = float(3000 / night)
    print("Rs.",prcStrd )

if room == "Deluxe":
    room_type = room.upper()
    prcdel = float(5000 / night)
    print("Rs.", prcdel)
if room == "Suite":
    room_type= room.upper()
    prcSut = float(8000 / night)
    print("Rs.",prcSut)





#Student result System
eng = float(input("Enter your English sub marks: "))
mth = float(input("Enter your Math sub marks: "))
scnc = float(input("Enter your Science sub marks: "))
cmptr = float(input("Enter your Computer sub marks: "))

avg = float(eng + mth + scnc + cmptr) / 4
print(f"Your average marks: {avg}")
if avg >= 80:
    print("Distinction")
elif avg >= 60:
    print("First Division")
elif avg >=50:
    print("Second Division")
elif avg >= 40:
    print("Pass")
else:
    print("Fail")