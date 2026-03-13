# Get user's name
name = input("Enter your name: ")

# Get age input (example: 22 years 3 months)
age_input = input("Enter your age (e.g., 22 years 3 months): ")

# Convert age to integer (years only)
age = int(age_input.split()[0])

# Calculate age in 2030 (assuming current year is 2026)
age_2030 = age + 4

# Display result
print(f"Hey {name}, you will be {age_2030} years old in 2030!")