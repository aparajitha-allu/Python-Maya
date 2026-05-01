# Input: Read the basic salary
basic_salary = int(input().strip())

# Determine DA and HRA percentages based on salary brackets
if basic_salary <= 10000:
    da = 0.80 * basic_salary
    hra = 0.20 * basic_salary
elif basic_salary <= 20000:
    da = 0.90 * basic_salary
    hra = 0.25 * basic_salary
else:
    # basic_salary > 20000
    da = 0.95 * basic_salary
    hra = 0.30 * basic_salary

# Calculate Gross Salary
gross_salary = basic_salary + da + hra

# Output: Display with 2 decimal places
print(f"{gross_salary:.2f}")