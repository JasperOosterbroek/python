def inlezen_beginstation(stations):
    beginstation = input('Wat is je beginstation? ')
    while(beginstation not in stations):
        beginstation = input('Dit station bestaat niet!\nVul je begin station in: ')
    return beginstation
def inlezen_eindstation(stations,beginstation):
    eindstation = input('Wat is je eindstation? ')
    while (eindstation not in stations or beginstation == eindstation):
        if eindstation == beginstation:
            eindstation = input('Dit station is al je beginstation.\nWat is je eindstation? ')
        else:
            eindstation = input('Deze trein komt daar niet!\nWat is je eindstation?: ')
    return eindstation

def omroepen_reis(stations,beginstation,eindsttion):
    numberOfStations = abs(stations.index(beginstation) - stations.index(eindstation))
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation,stations.index(beginstation)+1))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, stations.index(eindstation) + 1))
    print('De afstand bedraagt {} station(s).'.format(numberOfStations))
    print('De prijs van het kaartje is {} euro'.format(numberOfStations*5))
    print('Jij stapt in de trein in: {}'.format(beginstation))
    if stations.index(beginstation) > stations.index(eindstation):
        for i in range(stations.index(beginstation)-1, stations.index(eindstation), -1):
            print('- {}'.format(stations[i]))
    else:
        for i in range(stations.index(beginstation)+1, stations.index(eindstation), 1):
            print('- {}'.format(stations[i]))
    print('Jij stapt uit in: {}'.format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert','Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)