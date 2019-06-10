import numpy as np
import csv


with open('TM_Ex1.csv', newline='') as sb:
    kickprojects = csv.DictReader(sb)

for i in kickprojects:
    print(i["name"])


import csv

with open('cool_csv.csv', newline='') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for i in cool_csv_dict:
    print(i["Cool Fact"])