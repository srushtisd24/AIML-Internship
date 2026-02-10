search_name = input("Enter name to search: ")
with open("marks.txt", "r") as file:
    if search_name in file.read():
        print("found!")
    else:
        print("not found!")
