"""Project-Quiz Application"""
score = 0
print("Python Quiz")
q1= input("What is python ? ")
if q1.lower() == "programming language":
    score += 1
    print("Ans is correct")
else:
    print("Ans is wrong")
q2 = input("What data type is this (10)? ")
if q2.lower() == "tuple":
    score+=1
    print("Ans is correct")
else:
    print("Ans is wrong")
q3 = input("What is @property called ? ")
if q3.lower() == "decorator":
    score += 1
    print("Ans is correct")
else:
    print("Ans is wrong")

print("Quiz Finished")
print("Your total score out of 3 is",score)