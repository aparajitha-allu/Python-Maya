n = int(input())

square = n * n

# Convert to string and check ending
if str(square).endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")