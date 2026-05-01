# Read input
ch = input().strip()

# Convert to lowercase
ch = ch.lower()

# Check vowel or consonant
if ch in 'aeiou':
    print("VOWEL")
else:
    print("CONSONANT")