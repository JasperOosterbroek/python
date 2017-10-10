import csv
file = 'magazijn.csv'
with open(file, 'r') as scores:
    reader = csv.DictReader(scores,delimiter=';')
    mostExpensiveProductName = ''
    mostExpensiveProductPrice = 0
    leastAvailableProductAmount = 9999999
    leastAvailableProductId = 0
    totalProductAmount = 0

    for line in reader:
        totalProductAmount += int(line['Voorraad'])
        if mostExpensiveProductPrice < float(line['Prijs']):
            mostExpensiveProductPrice = float(line['Prijs'])
            mostExpensiveProductName = line['Naam']
        if leastAvailableProductAmount > int(line['Voorraad']):
            leastAvailableProductAmount = int(line['Voorraad'])
            leastAvailableProductId = int(line['Artikelnummer'])


print('Het duurste artikel is {} en die kost {} Euro\nEr zijn slechts {} exemplaren in voorraad van het product met nummer {}\nIn totaal hebben wij {} producten in ons magazijn liggen'.format(mostExpensiveProductName,mostExpensiveProductPrice,leastAvailableProductAmount,leastAvailableProductId,totalProductAmount))
