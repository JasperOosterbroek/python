import csv
file = 'highscore.csv'
with open(file, 'r') as scores:
    reader = csv.reader(scores,delimiter=';')
    highestName = ''
    highestNumber = 0
    highestDate = ''
    for row in reader:
        if highestNumber < int(row[2]):
            highestName = row[0]
            highestNumber = int(row[2])
            highestDate = row[1]

print('De hoogste score is: {} op {} behaald door {}'.format(highestNumber, highestDate,highestName))