import csv



dataset=[]

filename = 'GALEX_removed.csv'

with open(filename, 'r') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        # print(row)
         #for rows in row:
        dataset.append(row)
    print(dataset)  # we r getting each row and adding it list dataset . Now result is list of list
    
    