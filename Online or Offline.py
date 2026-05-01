# Input: N (online cost) and M (restaurant cost)
n, m = map(int, input().split())

# Calculate the discounted online price
discounted_online = n * 0.9

# Compare the costs
if discounted_online < m:
    print("ONLINE")
elif discounted_online > m:
    print("DINING")
else:
    print("EITHER")