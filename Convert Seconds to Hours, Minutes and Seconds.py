# Input
seconds = int(input())

# Conversion
hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
secs = remaining % 60

# Output
print(f"H:M:S-{hours}:{minutes}:{secs}")