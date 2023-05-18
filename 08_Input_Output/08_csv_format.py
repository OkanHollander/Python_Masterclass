import csv

csv_file = "OlympicMedals_2020.csv"
encoding = "utf-8"

with open(csv_file, encoding=encoding, mode='r', newline='') as f:
    headers = f.readline().strip('\n').split(',')
    print(f"Column headers: {headers}")
    reader = csv.reader(f)
    for row in reader:
        print(row)