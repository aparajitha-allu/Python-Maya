n = int(input().strip())

# Special case
if n <= 1:
    print("DEFICIENT")
else:
    total = 1  # 1 is always a proper factor

    # Find factors efficiently
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    # Compare
    if total == n:
        print("PERFECT")
    elif total < n:
        print("DEFICIENT")
    else:
        print("ABUNDANT")