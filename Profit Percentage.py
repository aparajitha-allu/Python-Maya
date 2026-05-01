# Input
cp, sp = map(int, input().split())

# Calculate profit percentage
profit_percent = ((sp - cp) / cp) * 100

# Output (2 decimal places)
print(f"{profit_percent:.2f}")