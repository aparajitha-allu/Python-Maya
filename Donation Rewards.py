# Input: Read the number of donations
x = int(input().strip())

# Determine the badge based on conditions
if x <= 3:
    print("BRONZE")
elif x <= 6:
    print("SILVER")
else:
    print("GOLD")
