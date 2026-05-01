n = int(input())
t = int(input())

even = n // 2
odd = n - even

filled_even = 0
filled_odd = 0

for _ in range(t):
    task = int(input())
    
    if task == 1:  # Fill all
        filled_even = even
        filled_odd = odd
    
    elif task == 2:  # Empty even
        filled_even = 0
    
    elif task == 3:  # Empty odd
        filled_odd = 0
    
    elif task == 4:  # Empty all
        filled_even = 0
        filled_odd = 0

# Total filled buckets
print(filled_even + filled_odd)