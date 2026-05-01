# Read input
X, Y, P = map(int, input().split())

# Check condition
if abs(X - Y) % (2 * P) == 0:
    print("YES")
else:
    print("NO")