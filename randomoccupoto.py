import csv
import random

occupations = {}

total_percentage = None # They don't quite add to 100%

with open('occupations.csv','r') as csvfile:
    words = csv.reader(csvfile)
    for row in words:
        if row[0] == "Total":
            total_percentage = float(row[1])
        elif row[0] != "Job Class":
            # "Job Class" is the first row, with only headings
            occupations[row[0]] = float(row[1])

def selectOccupation():
    randplace = random.random() * total_percentage
    curplace = 0.0
    last_job = None
    for job in occupations:
        curplace += occupations[job]
        last_job = job
        if curplace >= randplace:
            return job
    
    # This code is virtually never reached (at least not in millions of cases)
    # But if it does due to the selection of `randplace` and floating point
    # imprecision, just return a random job
    return random.choice(occupations.keys())

# Uses `selectOccupation` one million times to generate what
# `occupations` should look like. If they had different values,
# `selectOccupation` would be wrong
def test():
    frequencies = {}
    for job in occupations:
        frequencies[job] = 0

    cases = 1000000
    for _ in xrange(cases):
        selected = selectOccupation()
        frequencies[selected] += 1

    percentages = {}
    for job in frequencies:
        frequency = frequencies[job]
        percentages[job] = float(frequency) / float(cases) * total_percentage

    return percentages

