"""Project-Student Management System"""
Student = {}
while True:
    print("1.Add Student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Exit")
    choice = int(input("Enter your choice:"))    
    
    
    if choice == 1:
        roll = int(input("Enter roll no. :"))
        name = input("Enter name:")
        marks = int(input("Enter marks:"))
        Student[roll] ={
            "name": name,
            "marks":marks
        }
        print("Student data added successfully")
    elif choice == 2:
        if not Student:
            print("No student data available.")
        else:
            for roll,details in Student.items():
                print(f"Roll No: {roll}")
                print(f"Name:{details['name']}")
                print(f"Marks:{details['marks']}")
                print()
    elif choice == 3:
        roll = int(input("Enter roll number to be searched for:"))
        if roll in Student:
            print(Student[roll])
        else:
            print("Student doesn't exist")
    elif choice == 4:
        roll = int(input("Enter roll number to delete:"))
        if roll in Student:
            del(Student[roll])
        else:
            print("Student doesn't exist")
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Invalid choice")