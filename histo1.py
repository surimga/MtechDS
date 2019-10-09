import csv
import matplotlib.pyplot as plt


dataset=[]

filename = 'GALEX_removed.csv'

with open(filename, 'r') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        # print(row)
         #for rows in row:
        plt.hist(row[0])
        plt.show()
      #  dataset.append(row)
  # print(dataset)  # we r getting each row and adding it list dataset . Now result is list of list
