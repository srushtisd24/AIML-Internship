
name = input("Enter student name: ")
marks = input("Enter marks: ")
with open("marks.txt", "a") as file:
    file.write(f"{name} - {marks}\n")
with open("marks.txt", "r") as file:
    lines = file.readlines()
    count = len(lines)

print("Total number of records:", count)
