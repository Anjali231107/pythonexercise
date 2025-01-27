import random

def num_gaussing_game():
    print("Welcome")
    lower_bound = 1
    upper_bound = 200
    target_number = random.randint(lower_bound, upper_bound)
    max_attempts = 6
    attempts = 0

    print(f"Guess a number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess == target_number:
            print(f"Congratulations! You guessed the right number {target_number} in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        print(f"Attempts remaining: {max_attempts - attempts}")
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {target_number}.")


