# from datetime import datetime, timedelta
from datetime import datetime, timedelta

# Get the current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Extract individual components
current_date = current_datetime.date()
current_time = current_datetime.time()
print("Current Date:", current_date)
print("Current Time:", current_time)

# Format the current date and time
formatted_date = current_datetime.strftime("%B %d, %Y")
formatted_time = current_datetime.strftime("%H:%M:%S")
print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)

# Create a specific date
specific_date = datetime(2025, 1, 26, 13, 0)  # January 26, 2025 at 1 PM
print("Specific Date:", specific_date)

# Calculate a future date (e.g., 10 days from now)
future_date = current_datetime + timedelta(days=10)
print("Future Date (10 days later):", future_date)

# Calculate the difference between two dates
date_difference = future_date - specific_date
print("Difference between Future Date and Specific Date:", date_difference.days, "days")
