# Read input
units = int(input().strip())

# Calculate bill based on slabs
if units <= 199:
    bill = units * 1.20
elif units < 400:
    bill = units * 1.50
elif units < 600:
    bill = units * 1.80
else:
    bill = units * 2.00

# Apply surcharge
if bill > 400:
    bill = bill + (0.15 * bill)
else:
    bill = bill + 100

# Print result with 2 decimal places
print(f"{bill:.2f}")