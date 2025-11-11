# daily_reminder.py

# Ask the user for their task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine the reminder message based on priority using match case
match priority:
    case "high":
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"
    case _:
        priority_message = "task with unknown priority"

# Print a customized reminder based on time sensitivity
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time.")
