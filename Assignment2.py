print("Leap Year Checker")
year = int(input("Enter the year: "))
if((year%4 == 0) and (year%100 != 0 or year%400 == 0) ):
 print(f"{year} is a leap year")
else:
 print(f"{year} is not a leap year")

print("Login")
correct_username = "admin"
correct_password = "12345"

user_name = input("Enter your username: ")
user_password = input("Enter your Password: ")

if(correct_username == user_name):
    if(correct_password == user_password):
        print("Login successfull!!")
    else:
        print("wrong Password!!") 
else:
    print("wrong username!!")

char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter only one character.")
else:
    if char.isalpha():
        if char.lower() in 'aeiou':
            print("It is a vowel.")
        else:
            print("It is a consonant.")
    elif char.isdigit():
        print("It is a digit.")
    else:
        print("It is a special character.")

print("Simple Calculator")

value1 = int(input("Enter the 1st value: "))
value2 = int(input("Enter the 2nd value: "))
op = input("Enter the operator: ")
# check the operator 
match op:
    case "+" :
        print(value1 + value2)
    case "-" :
        print(value1 - value2)
    case "/" :
        print(value1 / value2)
    case "*" :
        print(value1 * value2)
    case _:
        print("enter a valid operator")

print("Electricity Bill")
time = input("May I comfirm whether this is your 1st bill or not in yes or no answern -> ")
unit = int(input("Enter the unit of electricity bill: "))
# to check for the first bill
if((time == "yes" )& (unit <= 100) ):
    print("For first time bill you have to pay Rs ",unit*5)
else:
    if(unit <= 100 or unit < 200 ):
        print("For electricity Bill you have to pay Rs ",unit*8)
    else:
        print("For electricity Bill you have to pay Rs ",unit*10)

print("Classify person into Age Group")
age = int(input("Enter your age: "))
if(age<13):
    print("You are child!!!")
elif(age>13 and age<=19):
    print("You are Teenager!!!!") 
elif(age>=20 and age<=59):
    print("You are Adult!!!")  
else:
    print("You are Senior!!!")  


print("Triangle Validator")
print("Enter the sides of the triangle ")
t1=int(input("Enter 1st side : "))
t2=int(input("Enter 2nd side : "))
t3=int(input("Enter 3rd side : "))

if(t1==t2==t3):
    print("It's Equilateral triangle")
elif((t1==t2 or t2==t3) or t1==t3):
    print("It's Isosceles triangle")
else:
    print("It's Scalene triangle") 


print("ATM Cash Withdrawal")
# Initial balance
balance = 5000

# Input: amount to withdraw
amount = int(input("Enter the amount to withdraw (in Rs.): "))

# Check for valid withdrawal
if amount <= 0:
    print("Invalid amount. Must be greater than 0.")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100.")
elif amount > balance:
    print("Insufficient balance.")
else:
    balance -= amount
    print(f"Withdrawal successful! Rs.{amount} withdrawn.")
    print(f"Remaining Balance: Rs.{balance}")
