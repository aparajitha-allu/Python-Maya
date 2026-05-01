# Read input
ch = input().strip()

# Check conditions
if 'A' <= ch <= 'Z':
    print("uppercase alphabet")
elif 'a' <= ch <= 'z':
    print("lowercase alphabet")
else:
    print("not an alphabet")