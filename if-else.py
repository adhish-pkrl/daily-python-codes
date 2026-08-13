####Basic IF-Else  

#Posite and Negative
num = int(input("ENter your number: "))
if num > 0:
    print("Your number is Positive!")
else:
    print("Your number is Negative!")


#Even or odd

if num % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is Odd!")


#Voting Eligibility
age = int(input("Enter your age: "))
if age >=18:
    print("You are eligible for Vote")
else:
    print("You are not eligible for Vote")


mrks = float(input("Enter your marks to check Pass or Fail!: "))
if mrks >=40:
    print("PAssed!")
else:
    print("Failed")


#Number Comparison
a = float(input("Enter a value of 'a': "))
b = float(input("Enter a value of 'b': "))
if a > b:
    print("'a' is greater then 'b'!")
else:
    print("'b' is greater then 'a'!")


#free Delivery
total_amount = float(input("Enter your Total Shopping Price: "))
if total_amount >=1000:
    print("You Got free delivery !")
else:
    print("Delivery Charge applies")


#Password Check
password = "pass123@"
if password == str(input("Enter a password: ")):
    print("Login Successful")
else:
    print("Password does not match")



#Temperature Check
temp = int(input("Enter the temperature: "))
if temp > 30:
    print("It's Hot !!")
else:
    print("Weather is Pleasant!")



#Divisible by 5
nm = int(input("Enter your number :"))
if nm % 5 == 0:
    print("the Number is Divisible by 5 !")
else:
    print("The number is not Divisible by 5 !")


#Largest of Two Numbers: 
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the Second number : "))
if num1>num2:
    print("num1 is grater teh num2")
elif num2 > num1 :
    print("num2 is greater then num1")
else:
    print("Both are Equal")

