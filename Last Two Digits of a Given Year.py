# Input
year = int(input())

# Get last two digits
last_two = year % 100

# Output (ensure 2 digits)
print(f"{last_two:02d}")