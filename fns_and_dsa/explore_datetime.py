#!/usr/bin/env python3

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date after {days_to_add} days: {formatted_future_date}")
        return future_date
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    current_date = display_current_datetime()
  
    calculate_future_date(current_date)
