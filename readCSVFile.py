import csv

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for i in cool_csv_dict:
    print(i["Ad name"])