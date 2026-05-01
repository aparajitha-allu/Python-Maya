# Read input
p, c, b, m, cs = map(int, input().split())

# Calculate percentage
percentage = (p + c + b + m + cs) / 5

# Determine grade
if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")