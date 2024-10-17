
import sys

class ATM:
    def __init__(self, pin):
        self.balance = 1000.0
        self.pin = pin
        self.transactions = []

    def authenticate(self):
        attempts = 0
        while attempts < 3:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("Authentication successful!\n")
                return True
            else:
                print("Incorrect PIN. Try again.")
                attempts += 1
        print("Too many failed attempts. Exiting.")
        sys.exit()

    def display_menu(self):
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Choose an option: ")
        return choice

    def check_balance(self):
        print(f"\nYour current balance is: ${self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("\nEnter the amount to deposit: "))
            if amount > 0:
                self.balance += amount
                self.transactions.append(f"Deposited: ${amount:.2f}")
                print(f"${amount:.2f} deposited successfully.")
            else:
                print("Invalid deposit amount.")
        except ValueError:
            print("Please enter a valid number for the deposit.")

    def withdraw(self):
        try:
            amount = float(input("\nEnter the amount to withdraw: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdrew: ${amount:.2f}")
                print(f"${amount:.2f} withdrawn successfully.")
            elif amount > self.balance:
                print("Insufficient funds.")
            else:
                print("Invalid withdrawal amount.")
        except ValueError:
            print("Please enter a valid number for the withdrawal.")

    def transaction_history(self):
        print("\nTransaction History:")
        if not self.transactions:
            print("No transactions available.")
        else:
            for transaction in self.transactions:
                print(transaction)

    def run(self):
        if self.authenticate():
            while True:
                choice = self.display_menu()
                if choice == '1':
                    self.check_balance()
                elif choice == '2':
                    self.deposit()
                elif choice == '3':
                    self.withdraw()
                elif choice == '4':
                    self.transaction_history()
                elif choice == '5':
                    print("Thank you for using the ATM. Goodbye!")
                    sys.exit()
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_pin = "1234"
    atm = ATM(user_pin)
    atm.run()
