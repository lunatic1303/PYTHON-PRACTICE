"""Problem-Create a student class"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = Student("Neha",20)
print(s1.name)

"""Problem-Bank Account class with deposit and withdraw methods"""
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,deposit):
        self.deposit = deposit
        return self.balance + self.deposit
    def withdraw(self,withdraw):
        self.withdraw = withdraw
        return self.balance - self.withdraw  
v = BankAccount(10000)
print("Balance after depositing money is",v.deposit(100))
print("Balance after withdrawing money is",v.withdraw(50))

"""Problem-Employee class"""
class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary = salary
    def Employee_details(self):
        print("Name of employee is:",self.name,"and employee's salary is:",self.salary)
e1 = Employee("Raj shamani",1500000)
e1.Employee_details()

"""Problem-Inheritance example"""
class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def breed(self):
        print("Dog breed is Labrador and its name is",self.name)
m1 = Dog("Buddy")
m1.breed()

"""Problem-Method overriding example"""
class Master:
    def __init__(self):
        print("This is master class")
    def n(self):
        print("This is master class method")
class Child(Master):
    def n(self):
        print("This is child class method")
j1 = Child()
j1.n()

"""Problem-Polymorphism example"""
print(len("Vansh"))
print(len([1,2,3,45]))
print(len((11,5,6)))

"""Problem-Abstract class example"""
from abc import ABC, abstractmethod
class non(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog:
    def sound(self):
        print("Bark")
        
"""Problem-super() example"""
class Student1:
    def __init__(self,name):
        self.name = name
class Student_update(Student1):
    def __init__(self,name,marks):
        self.marks= marks
        super().__init__(name)
r1 = Student_update("mh",98)
print(r1.name,r1.marks)


