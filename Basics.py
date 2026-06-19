"""Problem-Swap two numbers"""
a = 10
b = 20
a,b = b,a
print("The swapped numbers are",a,"and",b)

"""Problem-Check if a number is even or odd"""
n = int(input("Enter a number:"))
if n%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

"""Problem-Largest of three numbers"""
a1 = int(input("Enter first number:"))
b1 = int(input("Enter second number:"))  
c1 = int(input("Enter third number:"))
if a1>b1 and a1>c1:
    print("Largest number is",a1)
elif b1>a1 and b1>c1:
    print("Largest number is",b1)
else:
    print("Largest number is",c1)

"""Problem leap year checker"""
Year = int(input("Enter a year:"))
if (Year%4 == 0 and Year%100 != 0) or (Year%400 == 0):
    print(Year,"is a leap year")
else:
    print(Year,"is not a leap year")

"""Problem-Simple interest calculator"""
P = float(input("Enter principal amount:"))
R = float(input("Enter rate of interest:"))
T = float(input("Enter time in yrs:"))
SI = (P*R*T)/100
print("The simple interest is", SI)