#!/usr/bin/env python3

import sys
from bank_account import BankAccount

def main():
    # Check if sufficient arguments are provided
    if len(sys.argv) < 3:
        print("Usage: main-0.py <operation> <amount>")
        return

    # Create a new BankAccount instance
    account = BankAccount()

    # Parse command-line arguments
    operation = sys.argv[1].lower()
    try:
        amount = float(sys.argv[2])
    except ValueError:
        print("The amount should be a number.")
        return

    # Perform the requested operation
    if operation == "deposit":
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}")
    elif operation == "withdraw":
        if account.withdraw(amount):
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds for withdrawal.")
    elif operation == "balance":
        account.display_balance()
    else:
        print(f"Unknown operation: {operation}")
        print("Valid operations: deposit, withdraw, balance")

    # Display the current balance after operation
    account.display_balance()

if __name__ == "__main__":
    main()
