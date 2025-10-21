import random

def play_round():
    secret_number = random.randint(1, 10)
    number_of_guesses = 0
    print("\nI've picked a new number between 1 and 10.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            number_of_guesses += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:               
                print(f"Congratulations! You guessed it was {secret_number} in {number_of_guesses} guesses.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
while True:
    play_round()
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break