# Read input
X, A, B = map(int, input().split())

# Calculate total score
score = A * 1 + B * 2

# Check qualification
if score >= X:
    print("Qualify")
else:
    print("Not Qualify")