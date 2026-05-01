# Input
x = int(input())  # number of 5 rupee coins
y = int(input())  # number of 10 rupee coins
z = int(input())  # cost of one chocolate

# Total money
total = (5 * x) + (10 * y)

# Maximum chocolates
chocolates = total // z

# Output
print(chocolates)