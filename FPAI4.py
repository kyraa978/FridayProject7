# Define a dictionary of trivia questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest country in the world by land area?": "Russia",
    "What is the tallest mountain in the world?": "Mount Everest",
    "What is the largest organ in the human body?": "Liver",
    "What is the chemical symbol for gold?": "Au"
}

# Iterate through the questions and answers
for question, answer in questions.items():
    print(question)  # Print the question to the user
    user_answer = input("Your answer: ")  # Get the user's answer

    if user_answer.lower() == answer.lower():  # Check if the user's answer is correct (case-insensitive)
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", answer)