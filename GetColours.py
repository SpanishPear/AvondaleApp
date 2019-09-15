import csv
def getColours(colours):
    with open(colours) as e:
        for line in csv.DictReader(e):
            return line
print(getColours("SubjectColours.csv")["line1"])
