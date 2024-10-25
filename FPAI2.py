import random

# Import the `random` module to generate random numbers

# Greet the user
print("Welcome to the PowerBall Number Generator!")

# Generate random numbers for the five white balls (1-69)
white_ball1 = random.randint(1, 69)  # Generate a random number between 1 and 69
white_ball2 = random.randint(1, 69)  # Generate a random number between 1 and 69
white_ball3 = random.randint(1, 69)  # Generate a random number between 1 and 69
white_ball4 = random.randint(1, 69)  # Generate a random number between 1 and 69
white_ball5 = random.randint(1, 69)  # Generate a random number between 1 and 69

# Generate a random number for the red PowerBall (1-26)
red_ball = random.randint(1, 26)  # Generate a random number between 1 and 26

# Print the generated numbers in a formatted string
print(f"Your PowerBall numbers are: {white_ball1} {white_ball2} {white_ball3} {white_ball4} {white_ball5}   {red_ball}")

# Print a farewell message
print("Good luck!")