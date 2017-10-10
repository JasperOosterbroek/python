som = []
getal = eval(input('Geef een getal: '))
while getal != 0:
    som.append(getal)
    getal = eval(input('Geef een getal: '))
print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(som),sum(som)))