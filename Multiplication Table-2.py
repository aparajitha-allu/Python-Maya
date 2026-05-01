# Input: Read two space-separated integers A and B
# A represents the number (N), B represents the number of terms (R)
n, r = map(int, input().split())

# Loop from 1 up to (and including) r
for i in range(1, r + 1):
    # Calculate the product
    result = n * i
    # Print the output in the required format: n x i = result
    print(f"{n} x {i} = {result}")