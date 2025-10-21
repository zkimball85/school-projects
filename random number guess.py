import random
secret_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")
number_of_guesses = 0
while True:
    try:
        guess = int(input("Take a guess: "))
        number_of_guesses += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the secret number, which was", secret_number, "number of guesses", number_of_guesses)
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                break
            else:
                secret_number = random.randint(1, 10)
                number_of_guesses = 0
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
