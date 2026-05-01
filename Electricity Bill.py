# Read input
U = int(input().strip())

# Determine cost per unit
if U <= 199:
    cost = 1.20
elif U < 400:
    cost = 1.40
elif U < 600:
    cost = 1.60
elif U < 800:
    cost = 1.80
else:
    cost = 2.00

# Calculate bill
bill = U * cost

# Calculate surcharge
if bill > 400:
    surcharge = 0.15 * bill
else:
    surcharge = 0.00

# Total amount
total = bill + surcharge

# Print output
print(f"Units Consumed: {U}")
print(f"Cost per Unit: {cost:.2f}")
print(f"Bill: {bill:.2f}")
print(f"Surcharge: {surcharge:.2f}")
print(f"Total Amount: {total:.2f}")