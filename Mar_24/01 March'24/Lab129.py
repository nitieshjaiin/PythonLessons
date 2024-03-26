# how to read a csv file

import csv
with open("test.csv") as csvfile:
    read = csv.reader(csvfile)
    for row in read:
        print(row[0], row[1], sep= "|")

    csvfile.close()