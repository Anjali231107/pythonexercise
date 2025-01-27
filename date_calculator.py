from datetime import datetime, timedelta

def main():
    # Get the current date and time
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

    # Ask the user for a future date
    user_input = input("Enter a future date (YYYY-MM-DD): ")
    
    try:
        # Parse the user input into a datetime object
        future_date = datetime.strptime(user_input, "%Y-%m-%d")
        
        # Check if the entered date is in the past
        if future_date < now:
            print("The date you entered is in the past.")
        elif future_date == now:
            print("The date you entered is today.")
        else:
            # Calculate the difference in days
            difference = (future_date - now).days
            print(f"The date you entered is {difference} days away.")

            # Format and display the future date
            print("Formatted future date:", future_date.strftime("%A, %B %d, %Y"))

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
