import math

# Read number of test cases
T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    
    total = 0
    temp = n
    
    # Calculate sum of factorial of digits
    while temp > 0:
        digit = temp % 10
        total += math.factorial(digit)
        temp //= 10
    
    # Check condition
    if total == n:
        print("Strong")
    else:
        print("Not Strong")