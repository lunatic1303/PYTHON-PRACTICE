"""Project-Number Guessing Game"""
while True:
    import random
    number = float(input("Guess the number between 1 to 100:"))
    number1 = random.randint(1,100)

    if number == number1:
        print("You guessed the number right")
    elif number<number1:
        print("The number is greater than your guess")
    elif number>number1:
        print("The number is smaller than your guess")
    else:
        print("Oops,you guessed it wrong.\n Please try again!")
    again = input("Do you want to continue playing? (yes/no):")
    if again.lower() != "yes":
        break