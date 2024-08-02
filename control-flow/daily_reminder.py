#!/usr/bin/env python3


task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").strip().lower()

time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        task_info = f"'{task}' is a high priority task"
    case "medium":
        task_info = f"'{task}' is a medium priority task."
    case "low":
        task_info = f"'{task}' is a low priority task."
    case _:
        task_info = f"'{task}' has an undefined priority."

if time_bound == "yes":
    attention = "that requires immediate attention today!"
else:
    attention = "Consider completing it when you have free time."

print("Reminder:" if priority == "high" or priority == "medium" else "Note:", task_info, attention)
