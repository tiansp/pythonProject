import csv

with open("interface.csv", encoding='utf-8-sig') as f:
    csv_f = csv.DictReader(f)
    for i in csv_f:
        print(i)
