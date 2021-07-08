from sys import argv
import csv
with open('bakery.csv', 'a+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(argv)


