# MadLib Program with comments

# Prompt the user to enter the first adjective and store the input in the variable 'adjective1'
adjective1 = input("Enter an adjective: ")

# Prompt the user to enter the second adjective and store the input in the variable 'adjective2'
adjective2 = input("Enter another adjective: ")

# Prompt the user to enter the third adjective and store the input in the variable 'adjective3'
adjective3 = input("Enter one more adjective: ")

# Prompt the user to enter a large object and store the input in the variable 'large_object'
large_object = input("Enter a large object: ")

# Prompt the user to enter a small object and store the input in the variable 'small_object'
small_object = input("Enter a small object: ")

# Prompt the user to enter a place and store the input in the variable 'place'
place = input("Enter a place: ")

# Define a string that uses the user's inputs to create a MadLib story
# The 'f' before the quotes allows us to use variables directly inside the string
madlib = f"""
Once upon a time, in a {adjective1} land far away, there was a giant {large_object}.
People from all around would come to see this {adjective2} sight.
One day, a brave traveler brought a {small_object} with them to the {place}.
Everyone thought it was {adjective3}, but it changed the world forever.
"""

# Output the completed MadLib story to the screen
print(madlib)
