"""Problem-Division by zero exception handling"""
num = int(input("Enter number:"))
try:
    result = num/0
    print("Result is",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

"""Problem-Multiple exception handling"""
i = int(input("Enter value:"))
n = int(input("Enter some value:"))
try:
    m = i/n
    print("Value after division is:",m)
except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Entered value is not an integer")

"""Problem-File not found error handling"""
try:
    with open("neha.txt","r") as f:
        f.read()
except FileNotFoundError:
    print("File does not exist")

