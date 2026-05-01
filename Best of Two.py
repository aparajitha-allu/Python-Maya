# Read input
A1, A2, A3, B1, B2, B3 = map(int, input().split())

# Alice's score (top 2 of 3)
alice_rolls = sorted([A1, A2, A3])
alice_score = alice_rolls[1] + alice_rolls[2]

# Bob's score (top 2 of 3)
bob_rolls = sorted([B1, B2, B3])
bob_score = bob_rolls[1] + bob_rolls[2]

# Compare scores
if alice_score > bob_score:
    print("Alice")
elif bob_score > alice_score:
    print("Bob")
else:
    print("Tie")