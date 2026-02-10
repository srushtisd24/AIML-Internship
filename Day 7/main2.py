import csv

with open("C:\\Users\\srush\\OneDrive\\Desktop\\AIML Internship\\AIML-Internship\\Day 7\\company_Data.csv", mode="r") as file:
    csv_file = csv.reader(file)
    for lines in csv_file:
        print(lines) 

    