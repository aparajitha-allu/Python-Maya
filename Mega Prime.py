# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Read input
n = int(input().strip())

# Check if number is prime
if not is_prime(n):
    print("Not Mega Prime")
else:
    # Check if all digits are prime digits
    prime_digits = {'2', '3', '5', '7'}
    
    if all(d in prime_digits for d in str(n)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")