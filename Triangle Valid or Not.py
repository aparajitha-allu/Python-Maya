# Read input
a, b, c = map(int, input().split())

# Check triangle validity
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")