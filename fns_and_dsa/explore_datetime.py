from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()

    # Print formatted current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Ask user for number of days to add
    days = int(input("Enter the number of days to add to the current date: "))

    # Get current date
    current_date = datetime.now()

    # Calculate future date
    future_date = current_date + timedelta(days=days)

    # Print formatted future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

