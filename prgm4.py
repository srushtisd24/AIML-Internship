name = input("Enter your name: ")

years = int(input("Enter your age in years: "))
months = int(input("Enter additional months: "))


current_age = years + (months / 12)

age_2030 = current_age + 4

print(f"Hey {name}, you will be approximately {age_2030:.1f} years old in 2030!")