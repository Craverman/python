
import csv
num_rows = 0
with open('bakery.csv', encoding='utf8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[-1])



