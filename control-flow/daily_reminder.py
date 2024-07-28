#!/usr/bin/env python3


task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").strip().lower()


time_bound = input("Is it time-bound? (yes/no): ").strip().lower()


reminder = ""

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is of high priority."
    case "medium":
        reminder = f"Reminder: '{task}' is of medium priority."
    case "low":
        reminder = f"Note: '{task}' is of low priority."
    case _:
        reminder = f"Note: '{task}' has an undefined priority."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(reminder)
