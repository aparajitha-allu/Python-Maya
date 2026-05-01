n = int(input().strip())

# Total numbers = 2^n
for i in range(2 ** n):
    # Convert to binary and pad with leading zeros
    print(format(i, '0{}b'.format(n)))