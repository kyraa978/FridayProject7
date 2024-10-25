Friday Project 7 Overview

Friday Project 1 Notes:

User Input:
The program uses input() to prompt the user for specific types of words (three adjectives, a large object, a small object, and a place).
Each user response is saved to a variable for later use in the story.
Variable Assignment:

Variables (adjective1, adjective2, adjective3, large_object, small_object, place) are used to store each of the user’s inputs.
These variables help organize and label each piece of input for easy access in the final story.
String Formatting with f-strings:

An f-string (f"""...""") is used to create the MadLib story.
The f-string allows for easy insertion of variables directly into the string by using {} brackets.
This formatting approach is clean and readable, especially for stories with many variable placeholders.
Story Template:

The story is written as a single string, where variable placeholders are used to dynamically insert user input.
The placeholders {adjective1}, {large_object}, etc., are replaced by the values of the corresponding variables when the program runs.
Output:

The print() function is used to display the complete MadLib story to the user.
The story is formatted with line breaks using triple quotes (""") for readability.
Readability:

Each line of code has a clear purpose, making the program easy to follow.
Comments (if added) explain the purpose of each line, improving readability and making it easier to understand for beginners.


Friday Project 2 Notes:

Import the random module: This line imports the random module, which provides functions for generating random numbers.
Print a welcome message: This line prints a friendly welcome message to the user.
Generate random numbers for white balls:
The next five lines use the random.randint() function to generate five random integers between 1 and 69, representing the five white balls in a PowerBall lottery.
Generate a random number for the red PowerBall:
This line generates a random integer between 1 and 26, representing the red PowerBall.
Print the generated numbers:
This line uses an f-string to format the output, including the generated numbers and spacing between them.
Print a farewell message:
This line prints a good luck message to the user.


Friday Project 3 Notes:

Greeting and User Input:
A welcome message is printed to the user.
The user is asked if they want to play.
The user's input is stored in the play variable.
Check User's Response:
An if statement checks if the user's input, converted to lowercase, is "no".
If the user says "no", a farewell message is printed, and the program ends.
Start the Guessing Game:
If the user says "yes", a random number between 1 and 10 is generated and stored in the secret_number variable.
The guess variable is initialized to 0.
Guessing Loop:
A while loop continues until the user's guess matches the secret_number.
The user is prompted to enter a guess.
The guess is compared to the secret_number:
If the guess is too low, a message is printed.
If the guess is too high, a message is printed.
If the guess is correct, a congratulatory message is printed, and the loop ends.


Friday Project 4 Notes:

Define a dictionary of questions and answers:
A dictionary named questions is created to store the trivia questions and their corresponding answers.
Each key-value pair in the dictionary represents a question and its correct answer.
Iterate through the questions and answers:
A for loop is used to iterate through each key-value pair in the questions dictionary.
In each iteration, the question variable stores the current question, and the answer variable stores the correct answer.
Print the question:
The current question is printed to the console using the print() function.
Get the user's answer:
The input() function is used to prompt the user to enter their answer. The user's input is stored in the user_answer variable.
Check the answer:
The user's answer is compared to the correct answer, ignoring case differences using lower().
If the answers match, a "Correct!" message is printed.
If the answers don't match, an "Incorrect" message is printed along with the correct answer.

Friday Project 5:
red_text, blue_text, green_text, yellow_text, brown_text:
These functions take a text string as input.
They use ANSI escape sequences to format the text with the specified color.
The returned formatted text includes the ANSI codes to change the color in the terminal.
Main Function:

while True:: Creates a loop to allow multiple text colorings.
color_choice = input(...): Prompts the user to enter a color choice.
text = input(...): Prompts the user to enter the text to be colored.
if-elif-else block:
Checks the color_choice and calls the corresponding color function to print the colored text.
another_text = input(...): Asks the user if they want to color another text.
if another_text.lower() != "yes":: Checks if the user wants to stop the loop.
Overall, the code defines functions to color text using ANSI escape sequences and provides a user-friendly interface to input text and choose colors.


Friday Project 6 Notes:
**Summary of the Code:**

**BankAccount Class:**

* **`__init__(self, account_number, balance)`:** Initializes a new bank account instance with the given account number and balance.
* **`deposit(self, amount)`:** Adds the specified amount to the account balance and prints a confirmation message.
* **`withdraw(self, amount)`:** Subtracts the specified amount from the account balance if sufficient funds are available, otherwise prints an error message.
* **`check_balance(self)`:** Prints the current balance of the account.

**Main Program:**

* **Account Creation:** Creates a `BankAccount` instance with the specified account number and initial balance.
* **Main Loop:**
  - Prompts the user to enter their account number.
  - If the account number is correct, enters an inner loop:
    - Prompts the user to choose an option (deposit, withdraw, check balance, or exit).
    - Based on the user's choice, calls the appropriate method of the `BankAccount` instance.
  - If the account number is incorrect, prints an error message.



