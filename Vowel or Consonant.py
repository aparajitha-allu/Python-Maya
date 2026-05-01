# Read input
ch = input().strip()

# Convert to lowercase for easy comparison
ch = ch.lower()

# Check if vowel
if ch in ['a', 'e', 'i', 'o', 'u']:
    print("VOWEL")
else:
    print("CONSONANT")