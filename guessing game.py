secret_number = 25
guess = int(input("Guess the secret number (between 1 and 100): "))
if guess == secret_number:
    print("Congratulations! You guessed the secret number.")
elif guess < secret_number:
    print("Too low! Try again.")
elif guess > secret_number:
    print("Too high! Try again.")   
else:
    print("Invalid input. Please enter a number between 1 and 100.")