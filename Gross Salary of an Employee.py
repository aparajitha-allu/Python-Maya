# Input
salary = float(input())
hra = float(input())
da = float(input())

# Calculations
pf = 0.12 * salary
gross_salary = salary + hra + da + pf

# Output (2 decimal places)
print(f"{pf:.2f}")
print(f"{gross_salary:.2f}")