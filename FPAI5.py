def red_text(text):
  """Displays the given text in red color."""
  return f"\033[31m{text}\033[0m"  # Returns the text formatted with red color escape codes

def blue_text(text):
  """Displays the given text in blue color."""
  return f"\033[34m{text}\033[0m"  # Returns the text formatted with blue color escape codes

def green_text(text):
  """Displays the given text in green color."""
  return f"\033[32m{text}\033[0m"  # Returns the text formatted with green color escape codes

def yellow_text(text):
  """Displays the given text in yellow color."""
  return f"\033[33m{text}\033[0m"  # Returns the text formatted with yellow color escape codes

def brown_text(text):
  """Displays the given text in brown color."""
  return f"\033[33m{text}\033[0m"  # Returns the text formatted with brown color escape codes

def main():
  """Main function to handle user input and color output."""
  while True:  # Loop to allow multiple text colorings
    color_choice = input("Choose a color (red, blue, green, yellow, brown): ")  # Prompt user for color choice
    text = input("Enter the text: ")  # Prompt user for text to color

    if color_choice == "red":
      print(red_text(text))  # Print the text in red
    elif color_choice == "blue":
      print(blue_text(text))  # Print the text in blue
    elif color_choice == "green":
      print(green_text(text))  # Print the text in green
    elif color_choice == "yellow":
      print(yellow_text(text))  # Print the text in yellow
    elif color_choice == "brown":
      print(brown_text(text))  # Print the text in brown
    else:
      print("Invalid color choice. Please try again.")  # Handle invalid color choice

    another_text = input("Do you want to color another text? (yes/no): ")  # Ask if user wants to continue
    if another_text.lower() != "yes":  # Check if user wants to stop
      break

if __name__ == "__main__":
  main()  # Start the main function