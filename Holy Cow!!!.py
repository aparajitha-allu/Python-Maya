n, x = map(int, input().split())
cows = list(map(int, input().split()))

# Store prices of white cows
white_costs = []

for i in range(10):
    if cows[i] == 0:
        white_costs.append(i + 1)

# Sort costs (cheapest first)
white_costs.sort()

count = 0

for cost in white_costs:
    if n >= cost:
        n -= cost
        count += 1
    else:
        break

if count >= x:
    print("Happy")
else:
    print("Sad")