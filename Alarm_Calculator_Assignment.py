# 24 hour alarm calculations
# This allows a user to enter in the current time and then how long to wait before
# the alarm would go off

# Ask user to enter current time and how many hours to wait
print("\n")
current_time = int(input("Enter the current time (0-23): "))
wait_hours = int(input("Enter the number of hours to wait: "))
print("\n") 

# Do Calculations
addto_time = current_time + wait_hours
full_days = addto_time // 24
alarm_time = addto_time - (full_days * 24)

# Display the time the alarm would go off
print("Your alarm would go off at (24 hour time):", alarm_time)
print("\n") 
