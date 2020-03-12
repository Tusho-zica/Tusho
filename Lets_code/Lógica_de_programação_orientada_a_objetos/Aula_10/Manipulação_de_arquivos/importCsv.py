import csv
with open('./import.csv', 'r', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ';', quotechar='$')
    for row in spamreader:
        print(row)