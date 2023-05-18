import csv

cereal_filename = "cereal_grains.csv"

with open(cereal_filename, mode='r', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)