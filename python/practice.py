import csv
with open('marks.csv','r') as f:
    csvreader = csv.reader(f)
print(csvreader)    

