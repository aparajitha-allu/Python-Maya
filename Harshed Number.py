n = int(input())

# Find sum of digits
digit_sum = sum(int(d) for d in str(n))

# Check Harshad condition
if n % digit_sum == 0:
    print("True")
else:
    print("False")