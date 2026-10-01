
import csv

file_path = input("Enter the file path: ").strip('"\'')

with open(file_path, "r", encoding="utf-8") as file:
    read_file = csv.reader(file)

count = 0

for row in read_file:
    print(row)
    count +=1

    if count ==3:
        breakpoint


