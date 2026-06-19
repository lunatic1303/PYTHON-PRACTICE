"""Problem-Multiplication table of a number"""
num = int(input("Enter a number:"))
for i in range(1,11):
    print(num , "X", i , "=",num*i)

"""Problem-Factorial of number"""
fact = 1
n = int(input("Enter a number:"))
for i in range(1,n+1):
    fact = fact*i
print("Factorial of given number",n,"is",fact)

"""Problem-Fibonacci series"""
v = int(input("Enter number:"))
a = 0
b = 1
for i in range(v):
    print(a,end = " ")
    a,b = b,a+b

"""Problem-Prime number checker"""
num = int(input("Enter a number:"))
prime = True
for i in range(2,int(num**0.5)+1):
    if num%i == 0:
        prime = False
        break
if prime and num>1:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
