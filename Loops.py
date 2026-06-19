"""Problem-Multiplication table of a number"""
num = int(input("Enter a number:"))
for i in range(1,11):
    print(num , "X", i , "=",num*i)

"""Problem-Factorial of number"""
fact = 1
n = int(input("Enter a number:"))
for j in range(1,n+1):
    fact = fact*j
print("Factorial of given number",n,"is",fact)

"""Problem-Fibonacci series"""
v = int(input("Enter number:"))
a = 0
b = 1
for k in range(v):
    print(a,end = " ")
    a,b = b,a+b

"""Problem-Prime number checker"""
num = int(input("Enter a number:"))
prime = True
for m in range(2,int(num**0.5)+1):
    if num%m == 0:
        prime = False
        break
if prime and num>1:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

"""Problem-Armstrong number checker"""
arm = int(input("Enter number:"))
l = len(str(arm))
sum = 0
while arm>0:
    digit = arm%10
    sum+=digit**l
    arm//=10
if sum == arm:
    print(arm,"is an armstrong number")
else:
    print(arm,"is not an armstrong number")

"""Problem-Star printing program"""
b = int(input("Enter number:"))
for o in range(1,b+1):
    print("*"*o)
#Reverse star printing
for p in range(b,0,-1):
    print("*"*p) 