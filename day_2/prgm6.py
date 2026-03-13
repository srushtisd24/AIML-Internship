name = input("Enter your name: ")
age_input = input("Enter your age: ").split()

years = int(age_input[0])
months = int(age_input[2]) if len(age_input) > 2 else 0

age = years + (1 if months >= 6 else 0)
new_age = age + 4

print(f"Hey {name}, you will be {new_age} years old in 2030!")