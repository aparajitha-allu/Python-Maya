n = input().strip()

all_even = True
all_odd = True

for digit in n:
    d = int(digit)
    
    if d % 2 == 0:
        all_odd = False
    else:
        all_even = False

# Decide result
if all_even:
    print("Even")
elif all_odd:
    print("Odd")
else:
    print("Mixed")