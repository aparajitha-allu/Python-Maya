# Input: Read N (total members) and X (votes in favour)
n, x = map(int, input().split())

# Condition: Check if favour votes are half or more than half
if x >= n / 2:
    print("YES")
else:
    print("NO")