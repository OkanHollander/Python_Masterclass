import csv

csv_file = "Country_info.txt"
encoding = "utf-8"

with open(csv_file, encoding=encoding, mode="r", newline="") as f:
    sample = ""
    for line in range(3):
        sample += f.read()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    f.seek(0)
    reader = csv.reader(f, dialect=country_dialect)
    for row in reader:
        print(row)

print("*" * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace']
for att in attributes:
    print(f"{att}: {repr(getattr(country_dialect, att))}")
