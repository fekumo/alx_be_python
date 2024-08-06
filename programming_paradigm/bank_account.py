#!/usr/bin/env python3


class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        self._account_balance += amount

    def withdraw(self, amount):
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

    def get_balance(self):
        return self._account_balance
