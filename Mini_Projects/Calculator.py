"""Project-Calculator"""
while True:
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    print("Enter choice for calculation")
    print("1.For addition")
    print("2.For subtraction")
    print("3.For multiplication")
    print("4.For division")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1*num2)
    elif choice == 4:
        try:
            print(num1/num2)
        except ZeroDivisionError:
            print("Number cannot be divided by 0")
    else:
        print("Invalid choice")
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != "yes":  
        break


