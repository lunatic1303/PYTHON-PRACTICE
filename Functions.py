"""Problem-Factorial of a number using function"""
def f(num):
    fact = 1
    for el in range(1,num+1):
        fact*=el
    print(fact)
f(int(input("Enter number:")))

"""Problem-Prime number using function"""
def p(N):
    prime = True
    for el in range(2,int(N**0.5)+1):
        if N % el == 0:
            prime = False
            break
    if prime and N>1:
        print("Given number",N,"is prime")
    else:
        print("Given number",N,"is not prime")
p(int(input("Enter number:")))

"""Problem-Fibonacci using function"""
def fib(m):
    a = 0
    b = 1
    for el in range(m):
        print(a,end=" ")
        a,b = b, a+b
fib(int(input("Enter num:")))

"""Problem-Recursive factorial using function"""
def g(number):
    if number==0 or number==1:
        return 1
    return number * g(number-1)
print()
print("The factorial is",(g(5)))

"""Problem-Recursive fibonacci using factorial"""
def t(am):
    if am == 0:
        return 0
    elif am == 1:
        return 1
    return t(am-1) + t(am-2)
v = int(input("Enter number of terms:"))
for i in range(v):
    print(t(i),end=" ")