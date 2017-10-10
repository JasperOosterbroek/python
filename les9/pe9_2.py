import datetime
import csv

bestand = 'inloggers.csv'
#gebruik hier een herhalingslus:
while True:
    naam = input("Wat is je achternaam? ")
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    if len(naam) > 0 and len(voorl) > 0 and len(gbdatum) > 0 and len(email) > 0:
        break

with open(bestand, 'r') as inloggers:
    reader = csv.reader(inloggers,delimiter=';')
    for row in reader:
        if row[1] == voorl and row[2] == naam and row[3] == gbdatum and row[4] == email:
            exsist = True
            break
        else:
            exsist = False

if exsist == False:
    with open(bestand, 'a') as inloggers:
        writer = csv.writer(inloggers,delimiter=';', lineterminator='\n')
        today = datetime.datetime.now()
        time = today.strftime('%a %d %b %Y')
        timestring = "{} at {}:{}".format(time,today.hour,today.minute)
        writer.writerow((timestring,voorl,naam,gbdatum,email))
