class BankAccount:
    def __init__(self, account_number, balance):
        """Initializes a new BankAccount object with the given account number and balance."""
        self.account_number = account_number  # Stores the account number
        self.balance = balance  # Stores the account balance

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        self.balance += amount  # Adds the deposit amount to the balance
        print(f"Deposited ${amount}. New balance: ${self.balance}")  # Prints a confirmation message

    def withdraw(self, amount):
        """Withdraws the specified amount from the account, checking for sufficient funds."""
        if amount <= self.balance:  # Checks if there are enough funds
            self.balance -= amount  # Subtracts the withdrawal amount from the balance
            print(f"Withdrew ${amount}. New balance: ${self.balance}")  # Prints a confirmation message
        else:
            print("Insufficient funds.")  # Prints an error message

    def check_balance(self):
        """Prints the current balance of the account."""
        print(f"Your current balance is: ${self.balance}")

# Create an instance of the BankAccount class
account = BankAccount(12345, 1000)  # Creates an account with number 12345 and initial balance 1000

while True:
    user_input = input("Enter your account number (or 'quit' to exit): ")  # Prompts the user for their account number
    if user_input == 'quit':  # Checks if the user wants to quit
        break

    if user_input == account.account_number:  # Checks if the account number is correct
        while True:
            choice = input("Choose an option: (a) Deposit, (b) Withdraw, (c) Check Balance, (d) Exit: ")  # Prompts the user to choose an option
            if choice == 'a':
                amount = float(input("Enter the amount to deposit: "))  # Gets the deposit amount
                account.deposit(amount)  # Calls the deposit method
            elif choice == 'b':
                amount = float(input("Enter the amount to withdraw: "))  # Gets the withdrawal amount
                account.withdraw(amount)  # Calls the withdraw method
            elif choice == 'c':
                account.check_balance()  # Calls the check_balance method
            elif choice == 'd':
                break  # Exits the inner loop
            else:
                print("Invalid choice. Please try again.")  # Handles invalid input
    else:
        print("Incorrect account number. Please try again.")  # Handles incorrect account number