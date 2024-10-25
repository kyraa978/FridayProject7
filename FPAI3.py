import random

# Import the random module to generate random numbers

# Greet the user and ask if they want to play
print("Welcome to the Number Guessing Game!")  # Print a welcome message
play = input("Do you want to play? (yes/no): ")  # Ask the user if they want to play and store their answer

# Check if the user wants to play
if play.lower() == "no":  # Check if the user's input is "no" (case-insensitive)
    print("Maybe next time!")  # Print a farewell message if the user doesn't want to play
else:
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)  # Generate a random integer between 1 and 10

    guess = 0  # Initialize the guess variable

    # Start the guessing loop
    while guess != secret_number:  # Continue the loop until the guess is correct
        guess = int(input("Guess a number between 1 and 10: "))  # Get the user's guess and convert it to an integer

        if guess < secret_number:  # Check if the guess is too low
            print("Too low. Guess higher.")
        elif guess > secret_number:  # Check if the guess is too high
            print("Too high. Guess lower.")
        else:  # The guess is correct
            print("Congratulations! You guessed the correct number.")