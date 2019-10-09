import csv


dataset=[]

filename = 'GALEX_removed.csv'

with open(filename, 'r') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)
    print(row)    
    