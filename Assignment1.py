# Write a program in python that accepts the temperature in Fahrenheit
# from the user and coverts into degree Celsius.
# Formula:
# Celsius=5/9*(Fahrenheit-32)
# print("coverts Fahrenheit into degree Celsius.")
# Fahrenheit = int(input("Enter temperature in Fahrenhiet : "))
# Celsius=5/9*(Fahrenheit-32)
# print("celsius is : ",Celsius)

# Write a Python program that accepts the marks of 5 subjects from the
# user and calculates the total and percentage of the student.

# print("Enter the marks of five subject To calculates the " \
#        "total and percentage of the student")
# name = input("Enter name of a student: ") 
# s1 = int(input("Enter the Marks of Maths: "))
# s2 = int(input("Enter the Marks of Science: "))
# s3 = int(input("Enter the Marks of SST: "))
# s4 = int(input("Enter the Marks of Hindi: "))
# s5 = int(input("Enter the Marks of English: "))
# total= s1+s2+s3+s4+s5
# percentage = (total/500)*100
# print("Total marks obtaine out of 500 = ",total)
# print(f"Percentage of {name} = ",percentage)

# Write a program in Python that calculates the area and perimeter of a
# rectangle
# l=int(input("Enter the length of rectangle: "))
# b=int(input("Enter the breadth of rectangle: "))
# perimeter = (l+b)*2
# area = l*b
# print("Perimeter = ",perimeter)
# print("Area = ",area)

# Discuss Bitwise operators in Python along with examples.
print("Bitwise operators operate on binary representations of integers.")
print("Types of bitwise operator are:")
band = 5 & 3 
print("1. \" & \"  AND bitwise operator          ->   1 if both bits are 1                          ->       ",band)
bOr = 5 | 3 
print("2. \" | \"  OR bitwise operator           ->   1 if either bit is 1                          ->       ",bOr)
bxor = 	5 ^ 3
print("3. \" ^ \"  XOR bitwise operator          ->   1 if bits are different                       ->       ",bxor)
bnot = ~5 
print("4. \" ~ \"  NOT bitwise operator          ->   Inverts all bits (1s to 0s and 0s to 1s)      ->       ",bnot)
bLS = 	5 << 1 
print("5. \" << \" Left Shift bitwise operator   ->   Shifts bits left by n (*2ⁿ)	              ->      ",bLS)
bRS = 	5 >> 1
print("6. \" >> \" Right Shift bitwise operator  ->   Shifts bits right by n (/2ⁿ)                  ->       ",bRS)