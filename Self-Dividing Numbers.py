def is_self_dividing(n):
    # Convert number to string to iterate through digits
    temp_str = str(n)
    
    # Check if '0' is in the number
    if '0' in temp_str:
        return False
    
    # Check if n is divisible by every digit
    for digit in temp_str:
        if n % int(digit) != 0:
            return False
            
    return True

# Input: Read lower and upper bounds
a, b = map(int, input().split())

# Find all self-dividing numbers in the range [a, b]
result = []
for num in range(a, b + 1):
    if is_self_dividing(num):
        result.append(str(num))

# Output the result list as space-separated values
print(" ".join(result))