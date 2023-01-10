import csv

with open("./electronic-card-transactions-november-2022-csv-tables.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)