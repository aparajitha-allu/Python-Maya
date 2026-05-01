# Read input
X = int(input().strip())

# Check if possible
if X % 5 != 0:
    print(-1)
else:
    # Use maximum 10-rupee coins
    coins_10 = X // 10
    
    # Remaining amount
    remaining = X % 10
    
    # Use 5-rupee coins for remainder
    coins_5 = remaining // 5
    
    # Total coins
    print(coins_10 + coins_5)