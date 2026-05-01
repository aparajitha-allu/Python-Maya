# Read input
X = int(input().strip())
Y = int(input().strip())

# Total expenditure for 30 days
total = Y * 30

# Check if money is enough
if X >= total:
    print("YES")
else:
    print("NO")