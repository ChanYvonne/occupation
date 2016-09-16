import csv
import random

occupations = {}

with open('occupations.csv','r') as csvfile:
    words = csv.reader(csvfile)
    for row in words:
        if row[0] != "Job Class" and row[0] != "Total":
            occupations[row[0]] = float(row[1])

randplace = random.random()*100
curplace = 0.0
for job in occupations:
    percentage = occupations[job]
    if curplace >= randplace:
        print job
        break
    curplace += percentage

    
