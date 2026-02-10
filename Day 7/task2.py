import csv

with open("C:\\Users\\srush\\OneDrive\\Desktop\\AIML Internship\\AIML-Internship\\Day 7\\students.csv", "r") as file:
    reader = csv.DictReader(file) 

    print("Students who Passed:\n")

    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])